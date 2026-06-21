import pandas as pd

def export_to_excel(response_json):

    test_cases = response_json["test_cases"]

    df = pd.DataFrame(test_cases)

    print(df)

    df.to_excel(
        "outputs/generated_testcases.xlsx",
        index=False
    )

    print("Excel file generated successfully")