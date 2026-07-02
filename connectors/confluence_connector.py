from atlassian import Confluence

confluence = Confluence(
    url=CONFLUENCE_URL,
    username=EMAIL,
    password=TOKEN
)

page = confluence.get_page_by_id(
    page_id="12345",
    expand="body.storage"
)

requirement = page["body"]["storage"]["value"]