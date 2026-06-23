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