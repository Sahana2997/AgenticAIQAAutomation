import json
from openai import OpenAI
from dotenv import load_dotenv
from utils.prompt_loader import load_prompt

load_dotenv()
client = OpenAI()


def generate_locators(automation_steps, screen_xml):
    prompt_template = load_prompt("prompts/locator_prompt.txt")

    prompt = prompt_template.replace(
        "{automation_steps}",
        json.dumps(automation_steps, indent=4)
    )

    prompt = prompt.replace(
        "{screen_xml}",
        screen_xml
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    # Defensive cleanup (usually not needed with response_format)
    if content.startswith("```json"):
        content = content[len("```json"):].strip()

    if content.endswith("```"):
        content = content[:-3].strip()

    return json.loads(content)
