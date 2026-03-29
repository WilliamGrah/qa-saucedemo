from playwright.sync_api import Locator, Page
from tests.playwright.pages.cart_page import CartPage


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self, product_name: str) -> None:
        self.page.locator(f"[data-test='add-to-cart-{product_name}']").click()

    def remove_from_cart(self, product_name: str) -> None:
        self.page.locator(f"[data-test='remove-{product_name}']").click()

    def get_cart_badge(self) -> Locator:
        return self.page.locator("[data-test='shopping-cart-badge']")

    def get_all_product_names(self) -> list[str]:
        return self.page.locator("[data-test='inventory-item-name']").all_text_contents()

    def get_all_product_prices(self) -> list[float]:
        prices_text = self.page.locator("[data-test='inventory-item-price']").all_text_contents()
        return [float(price.replace("$", "")) for price in prices_text]

    def get_product(self, index: int) -> Locator:
        return self.page.locator("[data-test='inventory-item']").nth(index)

    def get_product_name(self, product: Locator) -> Locator:
        return product.locator("[data-test='inventory-item-name']")

    def get_product_description(self, product: Locator) -> Locator:
        return product.locator("[data-test='inventory-item-desc']")

    def get_product_price(self, product: Locator) -> Locator:
        return product.locator("[data-test='inventory-item-price']")

    def get_product_image(self, product: Locator) -> Locator:
        return product.locator("img")

    def click_product_title(self, product: Locator) -> None:
        return product.locator("[data-test='inventory-item-name']").click()

    def click_product_image(self, product: Locator) -> None:
        return product.locator("img").click()

    def sort_by(self, sort_type: str) -> None:
        self.page.locator("[data-test='product-sort-container']").select_option(sort_type)

    def go_to_cart(self):
        self.page.locator("[data-test='shopping-cart-link']").click()
        return CartPage(self.page)
