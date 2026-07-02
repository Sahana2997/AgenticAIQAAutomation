import os
from datetime import datetime

def save_screen_xml(driver, screen_name):
    os.makedirs("app_screens", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    driver.save_screenshot(f"resources/screenshots/{screen_name}_{timestamp}.png")
    page_source = driver.page_source
    file_path = f"resources/screens/{screen_name}.xml"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_source)

    return file_path

    print(f"saved screen xml to {file_path}")