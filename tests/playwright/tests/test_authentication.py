import pytest

from tests.playwright.pages.login_page import LoginPage
from playwright.sync_api import expect

BASE_URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"
LOCKED_USERNAME = "locked_out_user"

@pytest.mark.testcase("TC-AUTH-001")
def test_user_can_login_with_valid_credentials(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.testcase("TC-AUTH-002")
def test_user_cannot_login_with_invalid_username(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("invalid_username", VALID_PASSWORD)

    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

@pytest.mark.testcase("TC-AUTH-003")
def test_user_cannot_login_with_invalid_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_USERNAME, "12345")

    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

@pytest.mark.testcase("TC-AUTH-004")
def test_user_cannot_login_with_empty_username(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "12345")

    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Username is required"
    )

@pytest.mark.testcase("TC-AUTH-005")
def test_user_cannot_login_with_empty_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_USERNAME, "")

    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Password is required"
    )

@pytest.mark.testcase("TC-AUTH-006")
def test_locked_user_cannot_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(LOCKED_USERNAME, VALID_PASSWORD)

    expect(page.locator("[data-test='error']")).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )

@pytest.mark.testcase("TC-AUTH-007")
def test_logged_user_should_be_able_to_logout(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    page.locator("button#react-burger-menu-btn").click()
    page.locator("a[data-test='logout-sidebar-link']").click()

    expect(page).to_have_url(BASE_URL)

@pytest.mark.testcase("TC-AUTH-008")
def test_url_access_without_authentication(page):
    page.goto("https://www.saucedemo.com/inventory.html")

    expect(page).to_have_url(BASE_URL)

@pytest.mark.testcase("TC-AUTH-009")
def test_session_persistence_after_refresh(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    page.reload()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.testcase("TC-AUTH-010")
def test_session_persistence_across_tabs(page, context):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    new_page = context.new_page()
    new_page.goto("https://www.saucedemo.com/inventory.html")

    expect(new_page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.testcase("TC-AUTH-011")
def test_session_expiration_after_browser_close(page, context, browser):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    storage_state = context.storage_state()
    page.close()
    context.close()

    new_context = browser.new_context(storage_state=storage_state)
    new_page = new_context.new_page()
    new_page.goto("https://www.saucedemo.com/inventory.html")

    expect(new_page).to_have_url("https://www.saucedemo.com/inventory.html")
