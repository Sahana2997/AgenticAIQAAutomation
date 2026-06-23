import json

def save_testcases_json(response_json):

    with open("outputs/testcases/generated_testcases.json",
        "w"
        ) as file:
             json.dump(
                response_json,
                file,
                indent=4
             ) 

    print("Saved json")