from playwright.sync_api import sync_playwright
import os

def take_screenshots():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # Confirmation
        file_path = "file://" + os.path.abspath("/app/verification/mock_confirmation.html")
        page.goto(file_path)
        page.set_viewport_size({"width": 1280, "height": 1000})
        page.screenshot(path="/app/verification/v2_confirmation.png")
        
        # Success
        file_path = "file://" + os.path.abspath("/app/verification/mock_success.html")
        page.goto(file_path)
        page.screenshot(path="/app/verification/v2_success.png")
        
        browser.close()

if __name__ == "__main__":
    take_screenshots()
