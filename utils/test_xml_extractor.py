from tools.xml_extractor import (
    extract_locators
)

locators = extract_locators(
    "resources/screens/login_screen.xml"
)

for locator in locators:

    print(locator)

    