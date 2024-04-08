from playwright.sync_api import Playwright, sync_playwright, expect


def test3_counter_energy(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(6)").screenshot(path='output/3.png')
    context.close()
    browser.close()

with sync_playwright() as playwright:
    test3_counter_energy(playwright)
