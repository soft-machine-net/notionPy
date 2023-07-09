# Simpole Property Types
def handle_simple_property(property):
    property_type = property['type']
    return str(property[property_type])

def handle_checkbox(property):
    return handle_simple_property(property)

def handle_number(property):
    return handle_simple_property(property)

def handle_url(property):
    return handle_simple_property(property)

def handle_email(property):
    return handle_simple_property(property)

def handle_phone_number(property):
    return handle_simple_property(property)

def handle_created_time(property):
    return handle_simple_property(property)

def handle_last_edited_time(property):
    return handle_simple_property(property)


# MultiText Properties Types 
def handle_title(property):
    return ''.join(item['plain_text'] for item in property['title'])

def handle_multi_select(property):
    return ', '.join(item['name'] for item in property['multi_select'])

def handle_files(property):
    return ', '.join(file['name'] for file in property['files'])

def handle_relation(property):
    return ', '.join(item['id'] for item in property['relation'])

def handle_rollup(property):
    return property['rollup']['array']

def handle_rich_text(property):
    return ''.join(item['plain_text'] for item in property['rich_text'])


# User Property Types
def handle_common_user(property):
    property_type = property['type']
    return property[property_type]['id']

def handle_people(property):
    return ', '.join(person['id'] for person in property['people'])

def handle_created_by(property):
    return handle_common_user(property)

def handle_last_edited_by(property):
    return handle_common_user(property)


# Unique Property Types
def handle_formula(property):
    formula_type = property['formula']['type']
    return property['formula'][formula_type]

def handle_select(property):
    return property['select']['name']

def handle_status(property):
    return property['status']['name']

def handle_unique_id(property):
    prefix = property['unique_id']['prefix'] if property['unique_id']['prefix'] != None else ''
    return prefix + str(property['unique_id']['number'])

def handle_date(property):
    text = property['date']["start"]
    if property['date']['end'] is not None:
        text += "~" + property['date']['end']
    return text

def handle_unsupport_property(property):
    prop_type = property['type']
    return f"This property is not supported. TYPE:{prop_type}"