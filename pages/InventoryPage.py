class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_backpack = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart = page.locator("[data-test=\"shopping-cart-link\"]")

    def add_to_cart(self):
        self.add_backpack.click()

    def check_cart(self):
        self.cart.click()
