import re

# html_content = "<div class='dadsa'><p>This is a <a href='link.html'>link</a>.</p></div>"

# replaced_content = re.sub(r"<[^>]*>", "F", html_content)

# # print(replaced_content)


# # import re
# # html_content = "<html><html clas='asep'><html id='tes' class='tiny'><html style='color: red' id='yeet'>"

# # replaced_content = re.sub(r"<html[^>]*>", "a", html_content)

# # print(replaced_content)

# from bs4 import BeautifulSoup

# html_content = "<html class='wrong'><body><div class='another-wrong'></div></body></html><p>"

# valid_attributes = {
#     'html': ['class', 'id', 'style'],
#     'div': ['class', 'id', 'style']
# }

# k = "<html>"
# print(k.attrs)

# soup = BeautifulSoup(html_content, 'html.parser')
# print(soup)
# # for tag in soup.find_all(True):
# #     print(tag)
# #     for attr in tag.attrs:
# #         print(attr)
# #         if attr not in valid_attributes.get(tag.name, []):
# #             print(f"Invalid attribute '{attr}' in <{tag.name}> tag")



import re

import re

def normalize_html_tag(tag):
    # Replace multiple spaces with a single space
    tag = re.sub(r'\s+', ' ', tag)
    # Ensure no space before and one space after '=' in attributes
    tag = re.sub(r'\s*=\s*', '=', tag)

    if tag[len(tag)-2] == " ":
        tag = tag[0:len(tag)-2] + ">"
    return tag


def normalize_html_string(html_content):
    html_content= re.sub(r'<[^>]+>', lambda match: normalize_html_tag(match.group()),html_string )
    
    return html_content

html_string = "<p     class =                'kontol'       ></p> <div id=        \"\"></div>"
html_string = normalize_html_string(html_string)

print(html_string)

tag_pattern = r"<(\w+)([^>]*)>"
attr_pattern = r"(\w+)='([^']*)'|(\w+)=\"([^\"]*)\""

matches = re.finditer(tag_pattern, html_string)

for match in matches:
    tag_name = match.group(1)
    attributes = match.group(2)

    print("StartTag:", tag_name)

    for attr_match in re.finditer(attr_pattern, attributes):
        attr_name = attr_match.group(1) or attr_match.group(3)
        attr_value = attr_match.group(2) or attr_match.group(4)

        print("AttributeName:", attr_name, "AttributeValue:", attr_value)