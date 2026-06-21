from jira import JIRA

jira = JIRA(
    server="https://company.atlassian.net",
    basic_auth=(email, token)
)

issue = jira.issue("PROJ-123")

requirement = issue.fields.description