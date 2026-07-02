import xml.etree.ElementTree as ET


def extract_locators(xml_file):

    tree = ET.parse(xml_file)

    root = tree.getroot()

    candidates = []

    for element in root.iter():

        resource_id = element.attrib.get(
            "resource-id"
        )

        content_desc = element.attrib.get(
            "content-desc"
        )

        text = element.attrib.get(
            "text"
        )

        if (
            resource_id
            or content_desc
            or text
        ):

            candidates.append({

                "resource_id":
                    resource_id,

                "content_desc":
                    content_desc,

                "text":
                    text
            })

    return candidates