

from bs4 import BeautifulSoup
import re
# html : A
# head : B
# body : C
# title : D
# h1 : E
# h2 : F
# h3 : G
# h4 : H
# h5 : I
# h6 : J
# p : K
# em : L
# b : M
# abbr : N
# strong : O
# small : P
# div : Q
# table : V
# tr : W
# td : X
# th : Y
# link :
# script : R
# a : S
# img :
# button : T
# form : U
# input :

def replace_html_tags_with_letter(html_code, replacement_letter,tag_name):
    # Define a regular expression pattern to match HTML tags
    pattern = re.compile(f'<{tag_name}>')

    # Replace all HTML tags with the specified letter
    modified_html = re.sub(pattern, replacement_letter, html_code)

    return modified_html




def replace_tags_with_attribute(html_code, tag_name, attribute_name, replacement_letter):
    # Define a regular expression pattern to match the specified tag with the attribute
    pattern_string = '<{tag_name}\s+{attribute_name}=".*?".*?>'
    pattern = re.compile(fr'')
    

    # Replace the specified tags with the specified letter
    modified_html = re.sub(pattern, replacement_letter, html_code)

    return modified_html


def remove_content_tag(html_content):


    cleaned_html = re.sub(r'>[^<]+<', '><', html_content)

    # with open('cleanedtest.html', 'w') as file:
    #     file.write(cleaned_html)

    print(cleaned_html)
    return cleaned_html



def remove_content_except_head(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all tags except 'head' and remove their contents
    for tag in soup.find_all(lambda t: t.name != 'head'):
        tag.string = ''

    cleaned_html = str(soup)
    print(cleaned_html)
    return cleaned_html

def is_html_tag(tag):
    # Define a regular expression pattern for HTML tags
    pattern = re.compile(r'^<([a-zA-Z][^\s>]*)\s*[^>]*>$|^</([a-zA-Z][^\s>]*)\s*>$')
    match = pattern.match(tag)
    return bool(match)
    

def is_void_element(tag):
    # Define a regular expression pattern for void HTML elements
    pattern = re.compile(r'^<([a-zA-Z][^\s>]*)\s*[^>]*(?<!/)>$')
    
    # Use the pattern to match the tag
    match = pattern.match(tag)
    
    # Return True if it's a match, otherwise False
    return bool(match)

def remove_content(html_arr):
    not_allowed_text_in_tags = ["<head>","<html>","<body>","<div>","<table>",r"<link.*?>",]
    parent_tags = ["<body>","<head>","<html>",]


    initial_tag = ''
    parent_tag = ""
    for i in range(len(html_arr)):
        if is_html_tag(html_arr[i]):
            initial_tag = html_arr[i]
        else:
            if (initial_tag in not_allowed_text_in_tags or initial_tag[0:2] =='</'  or initial_tag == '')and html_arr[i] != ' ' :
                html_arr[i] = "<"
            else:
                html_arr[i] = ""

    return html_arr


def remove_space(tag):
    tag = re.sub(r'\s+', ' ', tag) # replace with single space
    tag = re.sub(r'\s*=\s*', '=', tag) # handle equals
    return tag

def remove_space_in_string(html_string):
    
    html_string = re.sub(r'<[^>]+>', lambda match: remove_space(match.group()), html_string)
    return html_string

def get_attributes(html_string):
    tag_pattern = r"<(\w+)([^>]*)>"
    attr_pattern = r"(\w+)='([^']*)'|(\w+)=\"([^\"]*)\""
    matches = re.finditer(tag_pattern, html_string)
    return_values = []
    for match in matches:
        tag_name = match.group(1)
        attributes = match.group(2)

        print("StartTag:", tag_name)

        for attr_match in re.finditer(attr_pattern, attributes):
            attr_name = attr_match.group(1) or attr_match.group(3)
            attr_value = attr_match.group(2) or attr_match.group(4)
            return_values.append((attr_name,attr_value))
    return return_values
# Example usage
html_content = """asfasd<html> <p>asdasdasd</p><head> <title>My Title</title><meta charset="utf-8"></head><body><h1>Hello World!</h1><p>This is a paragraph.</p><link>hello</body></html>"""
soup = BeautifulSoup(html_content, 'html.parser')

head_tag = soup.head

# k  = remove_content_tag(html_content)

html_string = "<html>scsdasd</html>"

# Use regular expression to find all HTML tags

tokens = re.findall(r'<[^>]+>|[^<]+', html_content)

print(remove_content(tokens))


# def checking(arr):
#     for i in arr:
#         if (is_void_element(i)):
#             print(i)
        


# checking(tokens)

