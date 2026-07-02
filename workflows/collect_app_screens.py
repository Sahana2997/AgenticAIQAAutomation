from appium import webdriver
from appium.options.common import AppiumOptions
from utils.screencapture import save_screen_xml

# Initialize Appium driver
options = AppiumOptions()
options.platform_name = "Android"  # or "iOS"
options.app = "/path/to/your/app.apk"  # Update with your app path
options.device_name = "emulator-5554"  # Update with your device name
options.automation_name = "UiAutomator2"  # or "XCUITest" for iOS

driver = webdriver.Remote("http://localhost:4723", options=options)

try:
    save_screen_xml(driver, "login_screen")
    
    driver.find_element(...).click()
    save_screen_xml(driver, "home_screen")
finally:
    driver.quit()
