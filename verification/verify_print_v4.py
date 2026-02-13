from playwright.sync_api import sync_playwright
import os

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Load mock print page
        abs_path = os.path.abspath("verification/mock_print.html")
        page.goto(f"file://{abs_path}")
        
        # Take screenshot
        page.screenshot(path="verification/v4_print.png", full_page=True)
        browser.close()

if __name__ == "__main__":
    run_verification()
