from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
client = OpenAI()

def generate_test_cases(requirement):
    prompt = f"""
    You are a Senior QA Engineer.
    Go through the given requirement dcoment - may be a JIRA Story or PRD Doment or the figma link and generate:
    1.Positive Test Cases
    2.Negative Test Cases
    3.Boundary Test Cases
    4.Validation Test Cases

    Requirement:
    {requirement}

    return ONLY valid JSON.
    Format:
    {{
        "test_cases":[
            {{
                "test_case_id":"TC001",
                "test_scenario":"",
                "test_case":"",
                "expected_result":""
            }}
        ]
    }}
    """
    response = client.chat.completions.create(
        model = "gpt-5",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    result = response.choices[0].message.content

    print(result , "Generate test case result")  # optional debugging

    return json.loads(result)