# def get_positive_testcases(response_json):
#     positive_testcases = []

#     for testcase in response_json["test_cases"]:

#         if testcase["test_scenario"].lower == "positive":
#             positive_testcases.append(testcase)

#     return positive_testcase
       
def is_automation_candidate(testcase):
    return (
        testcase["automation_candidate"]
        and testcase["priority"] == "High"
    )

def get_automation_testcases(testcases):
    automation_testcases = []
    for testcase in testcases:
        if is_automation_candidate(testcase):
            automation_testcases.append(testcase)


    return automation_testcases