from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #-------------------------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
