from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import io


def screenshot_post(i, post, padding_ratio=0.03):
    options = webdriver.ChromeOptions()
    options.headless = True
    browser = webdriver.Chrome(options=options)

    browser.get(post.url)

    # input("Press Enter to close the browser...")
    # browser.quit()

    wait = WebDriverWait(browser, 10)

    # Locate the post header
    post_header = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h1[slot='title']"))
    )

    # Get the size and position of the element
    location = post_header.location
    size = post_header.size

    # Calculate dynamic padding based on element's height
    padding = size["height"] * padding_ratio

    # Capture the entire page screenshot
    png = browser.get_screenshot_as_png()
    browser.quit()

    # Use PIL to process the image
    img = Image.open(io.BytesIO(png))

    # Define the area of interest with dynamic padding
    left = location["x"] - padding
    top = location["y"] - padding
    right = location["x"] + size["width"] + padding
    bottom = location["y"] + size["height"] + padding

    img = img.crop((left, top, right, bottom))
    img.save(f"title_screenshots/screenshot-{i}.png")
