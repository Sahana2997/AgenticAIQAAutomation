import os
import json
from agents.locator_agent import generate_locators

os.makedirs("outputs/locators", exist_ok=True)
with open("outputs/automation_steps/TC001_automation_steps.json") as file:
    automation_steps = json.load(file)
    #   content = file.read()

# print("File content:")
# print(repr(content))

with open("resources/screens/login_screen_one.xml") as file:
    login_screen_xml = file.read()
    
locator_result = generate_locators(automation_steps, login_screen_xml)
with open("outputs/locators/TC001_locators.json", "w") as file:
    json.dump(locator_result, file, indent=4)

print("Locator file generated successfully")