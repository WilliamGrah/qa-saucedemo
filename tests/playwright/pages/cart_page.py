from playwright.sync_api import Locator, Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def find_product(self, product_name: str) -> Locator:
        return self.page.locator("[data-test='inventory-item-name']") \
                        .filter(has_text=product_name)

    def total_products_in_cart(self) -> Locator:
        return self.page.locator("[data-test='inventory-item-name']")
