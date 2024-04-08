from playwright.sync_api import Playwright, sync_playwright, expect


def test1_counter_co2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(2)").screenshot(path='output/1.png')
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test1_counter_co2(playwright)
