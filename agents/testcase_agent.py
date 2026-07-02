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
    
    For each test case determine:
    automation_candidate = true

    IF:
    - Critical Business flow
    - Frequently executed
    - Stable
    - Repeatable

    automation_candidate = false

    IF:
    - Visual validation required
    - Rare edge case
    - Human judgement required
    - External dependency
    - Unstable Wrokflow

    Requirement:
    {requirement}

    return ONLY valid JSON.
    Format:
    {{
        "test_cases":[
            {{
                "test_case_id":"TC001", 
                "test_case":"",
                "automation_candidate": true,
                "automation_reson":"",
                "category": "",
                "priority":"",
                "expected_result":""
            }}
        ]
    }}
    """
    response = client.chat.completions.create(
        model = "gpt-5.4-mini",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )
    result = response.choices[0].message.content
    return json.loads(result)