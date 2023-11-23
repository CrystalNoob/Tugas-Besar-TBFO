

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

def replace_html_tag_all(html_tag):
    available_tags = ["html","head","body","title", "h1","h2","h3","h4","h5","h6","p","em","b","abbr","strong","small","div","table","tr","td","th"]
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'v', 'w', 'x', 'y', 'z']
    tags_void_without_attribute = ["br","hr"]
    available_tags_with_attribute = ["link","script","a","img","button","form","input"]
    attribute = [["rel", "href",] ,["src"] ,["href"], ["src","alt"],["type"],["action","method"],["type"]]
    symbols_tags_with_attribute = ["","r",'s', "",'t','u', ""]


    for i in range(available_tags):
        if available_tags[i] in html_tag:
            return symbols[i]
        
    for k in range(tags_void_without_attribute):
        if tags_void_without_attribute[k] in html_tag:
            return ""
    
    for j in range(len(available_tags_with_attribute)):
        if available_tags_with_attribute[j] in html_tag:
            return symbols_tags_with_attribute[j]
            


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
    need_values = ["type","method"]
    
    for match in matches:
        tag_name = match.group(1)
        attributes = match.group(2)
        print(f"name = {tag_name}")

        # print("StartTag:", tag_name)

        for attr_match in re.finditer(attr_pattern, attributes):
            attr_name = attr_match.group(1) or attr_match.group(3)
            attr_value = attr_match.group(2) or attr_match.group(4)
            if (attr_name in need_values):
                return_values.append((tag_name,attr_name,attr_value))
            else:
                return_values.append((tag_name,attr_name))
        
    return return_values

def check_if_valid(token):
    valid_attributes = {
        "html":[],
        "img":[("img","")]
    }



    global_attributes = [ "id", "class", "style"]
    globa_tag_names = ["html","head","body","title", "h1","h2","h3","h4","h5","h6","p","em","b","abbr","strong","small","div","table","tr","td","th","br","hr","link","script","a","img","button","form","input"]


    available_tags = ["html","head","body","title", "h1","h2","h3","h4","h5","h6","p","em","b","abbr","strong","small","div","table","tr","td","th"]
    symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'v', 'w', 'x', 'y', 'z']

    tags_void_without_attribute = ["br","hr"]
    available_tags_with_attribute = ["link","script","a","img","button","form","input"]
    attribute = [["rel", "href",] ,["src"] ,["href"], ["src","alt"],["type"],["action","method"],["type"]]
    symbols_tags_with_attribute = ["","r",'s', "",'t','u', ""]


    delimiter = "="
    pattern = f"({re.escape(delimiter)})"
    result = re.split(pattern, token)
    if len(result) != 1:
        print("disini 1")
        arr_sub = token.split(" ")
        print(arr_sub)
        for sub_section in arr_sub[1:]:
            if "=" not in sub_section:
                return False
        
        #checking for its attribtues
        attribute_values = get_attributes(token)

        print(attribute_values)
        is_correct = True
        if (len(attribute_values) == 0):
            return False
        for attribute in attribute_values:
            if (attribute[1] in global_attributes):
                pass
            else:
                if attribute in valid_attributes[attribute[0]]:
                    print("kesini")
                    pass
                else:
                    return False
        return True


    else:
        seperate_by_space = token.split(" ")
        print(seperate_by_space)
        if (len(seperate_by_space) != 1):
            return False
        else:
            
            pattern = r"<(\w+)>"
            match = re.search(pattern, token)
            if match.group(1) in globa_tag_names:
                return True
            else:
                False

    # attributes = get_attributes(token)
    # if ()



def tokenization(html_content):
    tokens = remove_space_in_string(html_content)
    tokens = tokens.replace(" >", ">")
    tokens = re.findall(r'<[^>]+>|[^<]+', tokens)
    tokens = remove_content(tokens)
    return tokens

    for token in tokens:
        pass

# Example usage
html_content = """asfasd<html> <p>asdasdasd</p><head> <title>My Title</title><meta charset="utf-8"></head><body><h1>Hello World!</h1><p>This is a paragraph.</p><link>hello</body></html>"""

token = tokenization(html_content)
print(token[5])
print(get_attributes("</p>"))
# # print(get_attributes(token[1]))
# print(check_if_valid(token[1]))
    





# def checking(arr):
#     for i in arr:
#         if (is_void_element(i)):
#             print(i)
        


# checking(tokens)

