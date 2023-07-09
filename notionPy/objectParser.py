import json
from . import parsers



def propertyToText(property):
    property_type = property['type']
    handler = getattr(parsers.property, f"handle_{property_type}", parsers.property.handle_unsupport_property)
    return handler(property)

def blockToText(block, isMarkdown=False):
    block_type = block["type"]
    handler = getattr(parsers.block , f"handle_{block_type}", parsers.block.handle_unsupport_block)
    return handler(block, isMarkdown)

def childrenToText(children, isMarkdown = False):
    text = ""
    for child in children['results']:
        text += blockToText(child, isMarkdown) + "\n"
    return text

def pageToText(page, isContainMetadata=False, properties = None ):
    # Metadata
    metadata_text = ""
    if isContainMetadata:
        metadata_text += f"Page URL: {page['url']}\n"
        metadata_text += f"Created Time: {page['created_time']}\n"
        metadata_text += f"Last Edited Time: {page['last_edited_time']}\n"
        metadata_text += f"Created By: {page['created_by']['id']}\n"
        metadata_text += f"Last Edited By: {page['last_edited_by']['id']}\n"
        metadata_text += f"Archived: {page['archived']}\n"
        metadata_text += f"Parent: {page['parent']['type']}\n"
        metadata_text += f"Cover: {page['cover']['url']}\n" if page['cover'] != None else ""

    properties_text = ""
    for prop_name, prop_value in page['properties'].items():
        if properties != None and not prop_name in properties:
            continue    
        properties_text += f"{prop_name}: {propertyToText(prop_value)}\n"
    return metadata_text + properties_text

def databaseToText(block):
    pass
