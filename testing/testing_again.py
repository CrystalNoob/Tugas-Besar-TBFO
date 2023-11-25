# import re
# html_content = '<html class="example" id="main"> <body style="background-color: #fff;"> <p>Some text</p> </body> </html>'

# # Define a regular expression pattern to match HTML tags and attributes
# pattern = r'<\s*([^/!\s>]+)(?:\s+([^>]+))?\s*>'

# matches = re.finditer(pattern, html_content)

# tag_list = []
# for match in matches:
#     tag_name = match.group(1)
#     tag_list.append(tag_name)

#     if match.group(2):
#         # Extract attributes if they exist
#         attributes = re.findall(r'([^\s=]+)\s*=\s*["\'](.*?)["\']', match.group(2))
#         for attr, value in attributes:
#             tag_list.append(attr)
#             tag_list.append(value)

# print(tag_list)


# import re

# def extract_tag_info(html_tag):
#     pattern = r'<\s*([^/!\s>]+)(?:\s*([^>]*))?\s*>'
#     matches = re.match(pattern, html_tag)
    
#     if matches:
#         tag_name = matches.group(1)
#         attributes = matches.group(2) if matches.group(2) else ""
#         attribute_list = re.findall(r'([^\s=]+)\s*=\s*(".*?"|\'.*?\'|\S+)', attributes)
        
#         result = [f'"{tag_name}"']
#         for attribute in attribute_list:
#             result.extend([attribute[0], "=", attribute[1]])
#         result.append('>')
#         return result
#     else:
#         return None

# # Test cases
# html_tag_1 = '<html class>'
# html_tag_2 = '<head class="" id="">'
# html_tag_3 = '<button id="2" class="life">'

# result_1 = extract_tag_info(html_tag_1)
# print(result_1[1])
# result_2 = extract_tag_info(html_tag_2)
# result_3 = extract_tag_info(html_tag_3)

# print(result_1)
# print(result_2)



# print(result_3)


import re

def remove_space(tag):
    tag = re.sub(r'\s+', ' ', tag) # replace with single space
    tag = re.sub(r'\s*=\s*', '=', tag) # handle equals
    return tag

def remove_space_in_string(html_string):
    
    html_string = re.sub(r'<[^>]+>', lambda match: remove_space(match.group()), html_string)
    return html_string

def tokenization(html_content):
    tokens = remove_space_in_string(html_content)
    tokens = tokens.replace(" >", ">")
    tokens = re.findall(r'<[^>]+>|[^<]+', tokens)
    final_tokens = []
    for token in tokens:
        if (token != "" and token):
            final_tokens.append(token)
    # tokens = remove_content(tokens)
    return tokens


def extract_tag_info(html_tag):
    pattern = r'<\s*([^/!\s>]+)(?:\s*([^>]*))?\s*>'
    matches = re.match(pattern, html_tag)
    #[['class', '']]  ada equals no value
    #['class'] no equels

    
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
        hasil = [tag_name]
        print(hasil)
        if (new_attributes[0] != ['']):
            for attribute in new_attributes:
                if len(attribute) >= 2:
                    if attribute[1] == '':
                        hasil.extend([attribute[0],"="])
                    else:
                        if (attribute[0] != "type" and attribute[0] != "method"):
                            hasil.extend([attribute[0],"=","TEXT"])
                        else:
                            hasil.extend([attribute[0],"=",attribute[1]])
                else:
                    hasil.extend([attribute[0]])
        return hasil
    
def string_to_one_line_demo(cont):
    lst=list(cont)
    str=''
    for i in lst:
        str+=i
        lst1=str.split("\n")
        str1=""

    for i in lst1:
        str1+=i+" "
        str2=str1[:-1]
    cont = str2
    return cont


path_to_data = "./data/"
path_to_html = "./data/acc.html"
path_to_text = ""
with open(path_to_html, 'r', encoding='utf-8') as html_file:
            html_content = html_file.read()
html_content = string_to_one_line_demo(html_content)
tokens = tokenization(html_content)

for token in tokens:
     print(token)
     hasil = extract_tag_info(token)
     print(hasil)