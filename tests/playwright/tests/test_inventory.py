import pytest

from tests.playwright.pages import inventory_page
from tests.playwright.pages.inventory_page import InventoryPage
from playwright.sync_api import expect
from tests.config import BASE_URL, INVENTORY_URL, VALID_USERNAME, \
    VALID_PASSWORD

@pytest.mark.testcase("TC-INV-001")
def test_should_display_products(logged_in):
    expect(logged_in.locator('.inventory_item')).to_have_count(6)

@pytest.mark.testcase("TC-INV-002")
def test_should_add_item_to_cart_when_button_clicked(logged_in):
    inventory_page = InventoryPage(logged_in)
    inventory_page.add_to_cart("sauce-labs-backpack")

    expect(inventory_page.get_cart_badge()).to_contain_text("1")

    cart_page = inventory_page.go_to_cart()
    expect(cart_page.find_product("Sauce Labs Backpack")).to_be_visible()

@pytest.mark.testcase("TC-INV-003")
def test_should_remove_from_cart_when_button_clicked(logged_in):
    selected_product = "sauce-labs-backpack"

    inventory_page = InventoryPage(logged_in)
    inventory_page.add_to_cart(selected_product)
    expect(inventory_page.get_cart_badge()).to_contain_text("1")

    inventory_page.remove_from_cart(selected_product)
    expect(inventory_page.get_cart_badge()).to_be_hidden()

    cart_page = inventory_page.go_to_cart()
    expect(cart_page.find_product(selected_product)).to_be_hidden()

@pytest.mark.testcase("TC-INV-004")
def test_should_add_multiple_products_in_cart(logged_in):
    inventory_page = InventoryPage(logged_in)

    products = ["sauce-labs-backpack", "sauce-labs-bike-light", "sauce-labs-fleece-jacket"]
    for product in products:
        inventory_page.add_to_cart(product)

    expect(inventory_page.get_cart_badge()).to_contain_text("3")

    cart_page = inventory_page.go_to_cart()
    expect(cart_page.total_products_in_cart()).to_have_count(3)

    expect(cart_page.find_product("Sauce Labs Backpack")).to_be_visible()
    expect(cart_page.find_product("Sauce Labs Bike Light")).to_be_visible()
    expect(cart_page.find_product("Sauce Labs Fleece Jacket")).to_be_visible()

@pytest.mark.testcase("TC-INV-005")
def test_product_should_display_informations(logged_in):
    inventory_page = InventoryPage(logged_in)

    product = inventory_page.get_product(0)

    expect(inventory_page.get_product_name(product)).to_contain_text("Sauce Labs Backpack")
    expect(inventory_page.get_product_description(product)).to_contain_text(
        "carry.allTheThings() with the sleek, streamlined Sly Pack that "\
        "melds uncompromising style with unequaled laptop and tablet protection."
    )
    expect(inventory_page.get_product_price(product)).to_contain_text("29.99")
    expect(inventory_page.get_product_image(product)).to_have_attribute("src", "/static/media/sauce-backpack-1200x1500.0a0b85a385945026062b.jpg")

@pytest.mark.testcase("TC-INV-006")
def test_when_click_product_name_it_should_redirect_to_product_page(logged_in):
    inventory_page = InventoryPage(logged_in)
    product = inventory_page.get_product(0)

    inventory_page.click_product_title(product)

    expect(logged_in).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")

@pytest.mark.testcase("TC-INV-007")
def test_when_click_product_image_it_should_redirect_to_product_page(logged_in):
    inventory_page = InventoryPage(logged_in)
    product = inventory_page.get_product(0)
    inventory_page.click_product_image(product)

    expect(logged_in).to_have_url("https://www.saucedemo.com/inventory-item.html?id=4")

@pytest.mark.testcase("TC-INV-008")
def test_when_click_sort_by_name_it_should_order_by_ascending(logged_in):
    inventory_page = InventoryPage(logged_in)
    inventory_page.sort_by("az")

    products_name = inventory_page.get_all_product_names()

    assert products_name == sorted(products_name)

@pytest.mark.testcase("TC-INV-009")
def test_when_click_sort_by_name_it_should_order_by_descending(logged_in):
    inventory_page = InventoryPage(logged_in)
    inventory_page.sort_by("za")

    products_name = inventory_page.get_all_product_names()

    assert products_name == sorted(products_name, reverse=True)

@pytest.mark.testcase("TC-INV-010")
def test_when_click_sort_by_price_low_to_high(logged_in):
    inventory_page = InventoryPage(logged_in)
    inventory_page.sort_by("lohi")
    products_prices = inventory_page.get_all_product_prices()

    assert products_prices == sorted(products_prices)

@pytest.mark.testcase("TC-INV-011")
def test_when_click_sort_by_price_high_to_low(logged_in):
    inventory_page = InventoryPage(logged_in)
    inventory_page.sort_by("hilo")
    products_prices = inventory_page.get_all_product_prices()

    assert products_prices == sorted(products_prices, reverse=True)
