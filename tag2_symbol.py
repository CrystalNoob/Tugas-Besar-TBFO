

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

# def replace_html_tags_with_letter(html_code, replacement_letter,tag_name):
#     # Define a regular expression pattern to match HTML tags
#     pattern = re.compile(f'<{tag_name}>')

#     # Replace all HTML tags with the specified letter
#     modified_html = re.sub(pattern, replacement_letter, html_code)

#     return modified_html

# def replace_html_tag_all(html_tag):
#     available_tags = ["html","head","body","title", "h1","h2","h3","h4","h5","h6","p","em","b","abbr","strong","small","div","table","tr","td","th"]
#     symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'v', 'w', 'x', 'y', 'z']
#     tags_void_without_attribute = ["br","hr"]
#     available_tags_with_attribute = ["link","script","a","img","button","form","input"]
#     attribute = [["rel", "href",] ,["src"] ,["href"], ["src","alt"],["type"],["action","method"],["type"]]
#     symbols_tags_with_attribute = ["","r",'s', "",'t','u', ""]


#     for i in range(available_tags):
#         if available_tags[i] in html_tag:
#             return symbols[i]
        
#     for k in range(tags_void_without_attribute):
#         if tags_void_without_attribute[k] in html_tag:
#             return ""
    
#     for j in range(len(available_tags_with_attribute)):
#         if available_tags_with_attribute[j] in html_tag:
#             return symbols_tags_with_attribute[j]
            


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


def squish_space(match):
    return f'{match.group(1)}="{match.group(2)}"'.replace(" ", "")


def squish_value(html_code):
    # print(html_code)
    pattern = r'(\w+)="([^"]*)"'
    modified_html = re.sub(pattern, squish_space, html_code)
    return modified_html


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
    # attr_pattern = r"(\w+)='([^']*)'|(\w+)=\"([^\"]*)\""
    # attr_pattern  =r'(\w+)=(\'[^\']*\'|"[^"]*")'
    attr_pattern = r'(\w+)=(\'[^\']*\'|"[^"]*"|[^\s>]+)'
    matches = re.finditer(tag_pattern, html_string)
    return_values = []
    need_values = ["type","method","class","id","sty"]
    
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


def get_attributes(html_string):
    tag_pattern = r"<(\w+)([^>]*)>"
    attr_pattern = r"(\w+)='([^']*)'|(\w+)=\"([^\"]*)\"" 
    matches = re.finditer(tag_pattern, html_string)
    return_values = []

    for match in matches:
        tag_name = match.group(1)
        attributes = match.group(2)

        for attr_match in re.finditer(attr_pattern, attributes):
            attr_name = attr_match.group(1)
            attr_value = attr_match.group(2).strip('\'"') if attr_match.group(2) else None

            return_values.append((tag_name, attr_name, attr_value))
    print(return_values)

    return return_values
        
    # return return_values




def tokenization(html_content):
    tokens = remove_space_in_string(html_content)
    # print(tokens)
    final_tokens = []
    final_result = []
    
    tokens = tokens.replace(" >", ">")
    tokens = re.findall(r'<[^>]+>|[^<]+', tokens)
    
    for token in tokens:
        if (token != ""  and not (token.isspace())):
            final_tokens.append(token)
    # tokens = remove_content(tokens)
    for token in final_tokens:
        final_result.extend(extract_tag_info(token))
    return final_result



def extract_tag_info(html_tag):
    html_tag = squish_value(html_tag)
    # print(html_tag)
    # <!---->
    if (len(html_tag) >= 7):
        if (html_tag[0:4] == "<!--" and html_tag[len(html_tag)-3:] == "-->"):
            return ['CMT'] 
    pattern = r'<\s*([^/!\s>]+)(?:\s*([^>]*))?\s*>'
    matches = re.match(pattern, html_tag)
    #[['class', '']]  ada equals no value
    #['class'] no equels

    
    if matches:
        tag_name = matches.group(1)
        attributes = matches.group(2) if matches.group(2) else ""
        # print(attributes)
        # print(attributes.split)
        attributes = attributes.split(" ")
        # print(attributes)
        new_attributes = []
        for att in attributes:
            att = att.split("=")
            new_attributes.append(att)
        
        # print(new_attributes)
        hasil = [tag_name]
        # print(hasil)
        if (new_attributes[0] != ['']):
            for attribute in new_attributes:
                if len(attribute) >= 2:
                    if attribute[1] == '':
                        hasil.extend([attribute[0],"="])
                    else:
                        if (attribute[0] != "type" and attribute[0] != "method"):
                            # hasil.extend([attribute[0],"=","TEXT"])
                            if (attribute[1][0] == attribute[1][len(attribute[1]) - 1]):
                                hasil.extend([attribute[0],"=","TEXT"])
                            else:
                                hasil.extend([attribute[0],"=",attribute[1]])
                        else:
                            hasil.extend([attribute[0],"=",attribute[1]])
                else:
                    hasil.extend([attribute[0]])
        hasil.extend([">"])
        return hasil
    else:
        pattern = r'</\s*([^/!\s>]+)(?:\s*([^>]*))?\s*>'
        matches = re.match(pattern, html_tag)
        if matches:
            tag_name = matches.group(1)
            attributes = matches.group(2) if matches.group(2) else ""
            attributes = attributes.split(" ")
            # print(attributes)
            new_attributes = []
            for att in attributes:
                att = att.split("=")
                new_attributes.append(att)
            
            # print(new_attributes)
            hasil = ["/"+tag_name]
            # print(hasil)
            if (new_attributes[0] != ['']):
                for attribute in new_attributes:
                    if len(attribute) >= 2:
                        if attribute[1] == '':
                            hasil.extend([attribute[0],"="])
                        else:
                            if (attribute[0] != "type" and attribute[0] != "method"):
                                if (attribute[1][0] == attribute[1][len(attribute[1]) - 1]):
                                    hasil.extend([attribute[0],"=","TEXT"])
                                else:
                                    hasil.extend([attribute[0],"=",attribute[1]])
                            else:
                                hasil.extend([attribute[0],"=",attribute[1]])
                    else:
                        hasil.extend([attribute[0]])
                
            return hasil
        else:
            return ["TEXT"]
        


# Example usage
# html_content = """<br/>"""

# token = tokenization(html_content)
# print(token)
# hasil = []
# for t in token:
#     k = extract_tag_info(t)
#     hasil.extend(k)
# print(hasil)


# def is_all_spaces(input_str):
#     return input_str.isspace()

# input_string = "    "
# if is_all_spaces(input_string):
#     print("The string consists of only spaces.")
# else:
#     print("The string contains characters other than spaces.")