def test_testcase1():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.avito.ru/avito-care/eco-impact")
        page.locator('.desktop-impact-items-F7T6E').scroll_into_view_if_needed()
        page.locator('.desktop-impact-items-F7T6E').screenshot(path=".output/testcase#1.png")
        browser.close()
