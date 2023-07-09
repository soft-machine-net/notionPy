import urllib.parse

# RichText Types
def handle_rich_text(block, isMarkdown = False):
    block_type = block['type']
    return ''.join(object['plain_text'] for object in block[block_type]['rich_text'])

def handle_bulleted_list_item(block, isMarkdown = False):
    markdown  = '- ' if isMarkdown else '' 
    return markdown + handle_rich_text(block)

def handle_paragraph(block, isMarkdown = False):
    markdown  = '' if isMarkdown else '' 
    return markdown + handle_rich_text(block)

def handle_heading_1(block, isMarkdown = False):
    markdown  = '# ' if isMarkdown else '' 
    return markdown + handle_rich_text(block)

def handle_heading_2(block, isMarkdown = False):
    markdown  = '## ' if isMarkdown else '' 
    return markdown + handle_rich_text(block)

def handle_heading_3(block, isMarkdown = False):
    markdown  = '### ' if isMarkdown else '' 
    return markdown + handle_rich_text(block)

def handle_numbered_list_item(block, isMarkdown = False, index = 1):
    markdown  = str(index)+'. ' if isMarkdown else '' 
    return markdown + handle_rich_text(block)

def handle_toggle(block, isMarkdown = False, markdown = '> '):
    markdown  = '> ' if isMarkdown else '' 
    return markdown + handle_rich_text(block)

def handle_callout(block, isMarkdown = False):
    markdown  = '> ' if isMarkdown else '' 
    return markdown + handle_rich_text(block).replace("\n", "\n"+markdown)

def handle_to_do(block, isMarkdown = False):
    markdown = '[x] ' if block['to_do']['checked'] else '[ ] ' 
    markdown = markdown if isMarkdown else ''
    return markdown + handle_rich_text(block)

def handle_code(block, isMarkdown = False):
    code_text = handle_rich_text(block)
    language = block["code"]["language"] if "language" in block["code"] else ""
    markdown = "```"
    return f"{markdown} {language}\n{code_text}\n{markdown}" if isMarkdown else code_text

def handle_quote(block, isMarkdown = False):
    markdown  = '> ' if isMarkdown else '' 
    return markdown + handle_rich_text(block).replace("\n", "\n"+markdown)



# File Types
def handle_common_file_type(block, isMarkdown = False):
    block_type = block['type']
    file_type = block[block_type]['type']
    url = block[block_type][file_type]['url']
    name = urllib.parse.urlparse(url).path.split('/')[-1] if isMarkdown else ''
    return f'[{name}]({url})' if isMarkdown else url

def handle_file(block, isMarkdown = False):
    return handle_common_file_type(block, isMarkdown)

def handle_image(block, isMarkdown = False):
    return handle_common_file_type(block, isMarkdown)

def handle_pdf(block, isMarkdown = False):
    return handle_common_file_type(block, isMarkdown)

def handle_video(block, isMarkdown = False):
    return handle_common_file_type(block, isMarkdown)



# Link Types
def handle_common_link(block, isMarkdown):
    block_type = block['type']
    url = block[block_type]['url']
    return f'[{url}]({url})' if isMarkdown else url

def handle_bookmark(block, isMarkdown = False):
    return handle_common_link(block, isMarkdown)

def handle_embed(block, isMarkdown = False):
    return handle_common_link(block, isMarkdown)

def handle_link_preview(block, isMarkdown = False):
    return handle_common_link(block, isMarkdown)



# UniqueT ypes
def handle_child_database(block, isMarkdown = False):
    if "child_database" in block and "title" in block["child_database"]:
        return "ChildDB: "+ block["child_database"]["title"]
    return ""

def handle_child_page(block, isMarkdown = False):
    title = block["child_page"]["title"]
    url = 'https://notion.so/' + block['id']
    return f'[{title}]({url})' if isMarkdown else title

def handle_divider(block, isMarkdown = False):
    return "\n---------------------------------------\n"

def handle_equation(block, isMarkdown = False):
    return block["equation"]["expression"]

# Table Types
def handle_table(block, isMarkdown = False):
    has_children = block['has_children']
    if has_children and 'children' in block:
        row =''.join(handle_table_row(child['table_row']) + "\n" for child in block['children'] )
        return row
    return handle_unsupport_block(block)

def handle_table_row(block, isMarkdown = False):
    text = ''
    for cell in block['cells']:
        text += ''.join(item['plain_text'] for item in cell)
        # text += cell[0]['plain_text']
    return text

def handle_unsupport_block(block, isMarkdown = False):
    block_type = block['type']
    return f"This block is not supported. TYPE:{block_type}"