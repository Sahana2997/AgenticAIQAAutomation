from agents.testcase_agent import generate_test_cases
from utils.excel_exporter import export_to_excel

requirement = """
As a user,
I want to login using mobile number and otp 
so that i can login on the application
"""
response_json = generate_test_cases(requirement)
print(type(response_json))


export_to_excel(response_json)
