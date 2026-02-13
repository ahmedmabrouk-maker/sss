from playwright.sync_api import sync_playwright
import os

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Load mock confirmation page
        abs_path = os.path.abspath("verification/mock_confirmation.html")
        page.goto(f"file://{abs_path}")
        page.screenshot(path="verification/v3_confirmation.png", full_page=True)

        # Load mock tracking page
        abs_path = os.path.abspath("verification/mock_tracking.html")
        page.goto(f"file://{abs_path}")
        page.screenshot(path="verification/v3_tracking.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run_verification()
