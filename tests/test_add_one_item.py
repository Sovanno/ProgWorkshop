from playwright.sync_api import Page, expect
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage

def test_add_one_item(page: Page) -> None:
    login_page = LoginPage(page)
    shop = InventoryPage(page)
    cart = CartPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    shop.add_to_cart()
    shop.check_cart()
    expect(cart.inventoty_item).to_have_count(1)
