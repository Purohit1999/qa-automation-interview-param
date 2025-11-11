# tests/test_e2e.py
from playwright.sync_api import Page, expect

BASE = "http://127.0.0.1:8000"

# A single task row looks like:
# <div class="list-group-item d-flex justify-content-between align-items-center">
#   <div class="flex-grow-1">TITLE …</div>
#   <div> <button>✓</button> <button>🗑️</button> </div>
# </div>
ROW = "div.list-group-item.d-flex.justify-content-between.align-items-center"
TITLE_CELL = "div.flex-grow-1"


def login(page: Page, username: str, password: str):
    page.goto(f"{BASE}/login/")
    expect(page.locator('input[name="username"]')).to_be_visible()
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url(f"{BASE}/dashboard/")


def task_rows(page: Page, title: str):
    # Match ONLY list rows that have a title cell containing the text
    return page.locator(
        f"{ROW}:has({TITLE_CELL}:has-text('{title}'))"
    )


def first_row(page: Page, title: str):
    return task_rows(page, title).first


def add_task(page: Page, title: str):
    task_input = page.locator("input[placeholder='Enter a new task...'], input[name='title']")
    expect(task_input).to_be_visible()
    task_input.fill(title)

    add_btn = page.get_by_role("button", name="Add Task", exact=False)
    if not add_btn.count():
        add_btn = page.get_by_role("button", name="Add", exact=False)
    add_btn.click()

    # Pagination-safe assertion: just ensure at least one matching row is visible.
    # (The newest row is at the top, so this will be true even if older duplicates moved off page 1.)
    expect(first_row(page, title)).to_be_visible()

def complete_task(page: Page, title: str):
    row = first_row(page, title)
    # Try checkbox or a ✓ button
    if row.locator("input[type='checkbox']").count():
        row.locator("input[type='checkbox']").check()
    elif row.locator("button:has-text('✓')").count():
        row.locator("button:has-text('✓')").first.click()


def delete_task(page: Page, title: str):
    # Remove all rows that match the title (in case duplicates exist)
    while task_rows(page, title).count():
        row = first_row(page, title)
        if row.locator("button:has-text('🗑️')").count():
            row.locator("button:has-text('🗑️')").first.click()
        elif row.get_by_role("button", name="Delete").count():
            row.get_by_role("button", name="Delete").first.click()
        else:
            row.locator("button").last.click()


def test_auth_logout(page: Page):
    login(page, "user1", "testpass123")
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url(f"{BASE}/login/")


def test_task_crud(page: Page):
    login(page, "user1", "testpass123")
    add_task(page, "Buy milk")
    expect(task_rows(page, "Buy milk")).to_have_count(1)

    complete_task(page, "Buy milk")
    delete_task(page, "Buy milk")
    expect(task_rows(page, "Buy milk")).to_have_count(0)


def test_isolation_between_users(page: Page):
    # user1 creates a task
    login(page, "user1", "testpass123")
    add_task(page, "U1 only task")
    page.get_by_role("link", name="Logout").click()
    expect(page).to_have_url(f"{BASE}/login/")

    # user2 logs in — MUST NOT see user1's task
    login(page, "user2", "testpass123")
    expect(task_rows(page, "U1 only task")).to_have_count(0)
