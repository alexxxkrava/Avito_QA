import os
import pytest
from playwright.sync_api import sync_playwright
from counter_params import counter_params

@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page

@pytest.mark.parametrize("data_tests, counter_selector, test_name", counter_params)
def test_counter_screenshot(browser_page, data_tests, counter_selector, test_name):
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    page = browser_page

    page.route('https://www.avito.ru/web/1/charity/ecoImpact/init', lambda route: route.fulfill(json=data_tests))

    page.goto('https://www.avito.ru/avito-care/eco-impact', timeout=60000)

    page.wait_for_timeout(3000)

    counter_element = page.locator(counter_selector)
    screenshot_path = os.path.join(output_folder, f"{test_name}.png")
    counter_element.screenshot(path=screenshot_path)

    page.close()
