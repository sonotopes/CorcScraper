from playwright.sync_api import sync_playwright
import time
from numpy import random


def extract_all_html(from_url, pages, wait_for=None):
    """Extracts raw html"""
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(from_url)
        html = None
        a = 0

        # Passing through each webpage. Default will be thirty pages but this can be changed to a max of 100.
        while a < pages:
            page.wait_for_load_state("networkidle")
            page.evaluate("() => window.scroll(0, document.body.scrollHeight)")
            page.wait_for_load_state("domcontentloaded")

            if wait_for:
                page.wait_for_selector(wait_for)

            if html:
                html += page.inner_html("body")
            else:
                html = page.inner_html("body")

            page.locator('"NEXT"').click()
            a += 1

            # To avoid cloudflare or other anti-scraping software, time between every click has to be randomized.
            time.sleep(random.choice([x / 10 for x in range(30, 67)]))

        return html
