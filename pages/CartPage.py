class CartPage:
    def __init__(self, page):
        self.page = page
        self.inventoty_item = page.locator("[data-test=\"inventory-item\"]")
