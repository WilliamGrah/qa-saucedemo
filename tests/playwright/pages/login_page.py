from playwright.sync_api import Page
from typing import Optional


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("input[data-test='username']")
        self.password_input = page.locator("input[data-test='password']")
        self.login_button = page.locator("input[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def navigate(self) -> None:
        self.page.goto("https://www.saucedemo.com")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> Optional[str]:
        return self.error_message.text_content()
