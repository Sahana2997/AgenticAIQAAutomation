import json
import os
from agents.automation_agent import generate_automation_steps
from utils.testcase_filter import get_automation_testcases



os.makedirs("outputs/automation_steps", exist_ok=True)

with open("outputs/testcases/generated_testcases.json") as file:
    data = json.load(file)

automation_testcases = get_automation_testcases(data["test_cases"])

for testcase in automation_testcases:
    automation_steps = generate_automation_steps(testcase, "mobile")
    filename = (f"outputs/automation_steps/{testcase['test_case_id']}_automation_steps.json")
    with open(filename, "w") as file:
        file.write(automation_steps)

    print(f"Saved:{filename}")
