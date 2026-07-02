import json

from openai import OpenAI
from dotenv import load_dotenv
from utils.prompt_loader import load_prompt

load_dotenv()
client = OpenAI()

def generate_automation_steps(testcase, platform):
    if platform.lower() == "web":
        prompt_template = load_prompt("prompts/selenium_prompt.txt")
    else:
        prompt_template = load_prompt("prompts/appium_prompt.txt")

    prompt = prompt_template.replace("{testcase}", str(testcase))

    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [
            {
                "role":"user",
            "content": prompt
            }
        ]
    )
    # content =  response.choices[0].message.content
    content = response.choices[0].message.content.strip()

    print("----- RAW LLM RESPONSE -----")
    print(content)
    print("----------------------------")

    return json.loads(content)
    # if content.startswith("```json"):
    #     content = content[len("```json"):].strip()

    # if content.endswith("```"):
    #     content = content[:-3].strip()

    # return json.loads(content)
