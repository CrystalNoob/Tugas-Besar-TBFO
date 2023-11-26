

from colorama import Fore, Style
import re
from miscellaneous import*

def replace_equals(match):
    inside_quotes = match.group(1)
    replaced_inside_quotes = inside_quotes.replace('=', 'X')
    return f'="{replaced_inside_quotes}"'


def normalize_html_file_content(html_content):

    pattern = re.compile(r"(<[^>]+)\n\s+")
    while pattern.search(html_content):
        html_content = pattern.sub(lambda m: m.group(1) + " ", html_content)
    return html_content

def squish_space(match):
    return f'{match.group(1)}="{match.group(2)}"'.replace(" ", "")

def squish_value(html_code):
    # print(html_code)
    pattern = r'(\w+)="([^"]*)"'
    modified_html = re.sub(pattern, squish_space, html_code)
    return modified_html

def remove_space(tag):
    tag = re.sub(r'\s+', ' ', tag) # replace with single space
    tag = re.sub(r'\s*=\s*', '=', tag) # handle equals
    return tag

def remove_space_in_string(html_string):
    
    html_string = re.sub(r'<[^>]+>', lambda match: remove_space(match.group()), html_string)
    return html_string

def tokenization(html_content):
    tokens = remove_space_in_string(html_content)
    # print(tokens)
    final_tokens = []
    final_result = []
    
    tokens = tokens.replace(" >", ">")
    tokens = re.findall(r'<[^>]+>|[^<]+', tokens)
    
    for token in tokens:
        if (not (token.isspace())):
            final_tokens.append(token)
    # tokens = remove_content(tokens)
    for token in final_tokens:
        final_result.extend(extract_tag_info(token))
    return final_result

def extract_tag_info(html_tag):
    pattern = r'="([^"]*)"'
    html_tag = re.sub(pattern, replace_equals, html_tag) # handle equal sign inside value
    
    html_tag = squish_value(html_tag)
    # print(html_tag)
    # <!---->
    if (len(html_tag) >= 7):
        if (html_tag[0:4] == "<!--" and html_tag[len(html_tag)-3:] == "-->"):
            return ['CMT'] 
    pattern = r'<([^/!\s>]+)(?:\s*([^>]*))?\s*>'
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
        pattern = r'</([^/!\s>]+)(?:\s*([^>]*))?\s*>'
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
        

def tokenization_for_a_line(html_content):
    tokens = tokens = remove_space_in_string(html_content)
    # print(tokens)
    final_tokens = []
    final_result = []
    
    tokens = tokens.replace(" >", ">") # get rid of final space behind closing tags (space that remove_space_in_string didn't handle)
    tokens = re.findall(r'<[^>]+>|[^<]+', tokens)
    
    for token in tokens:
        final_tokens.append(token)
    # tokens = remove_content(tokens)

    return final_tokens

