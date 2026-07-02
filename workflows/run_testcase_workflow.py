from agents.testcase_agent import generate_test_cases
from utils.excel_exporter import export_to_excel
from utils.json_exproter import save_testcases_json
from utils.testcase_filter import get_automation_testcases
import json

requirement = """
As a user,
I want to login using mobile number and otp 
so that i can login on the application
"""

#Calling Test Case Agent
response_json = generate_test_cases(requirement)

#save JSON
save_testcases_json(response_json)

# Save Excel
export_to_excel(response_json)

# get automation test cases from the locally saved JSON
with open("outputs/testcases/generated_testcases.json") as file:
    saved_response_json = json.load(file)

automation_testcases = get_automation_testcases(
    saved_response_json["test_cases"]
)

print(f"Automation test cases: {automation_testcases}")
