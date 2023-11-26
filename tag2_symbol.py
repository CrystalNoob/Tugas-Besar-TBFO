

from bs4 import BeautifulSoup
import re


def squish_space(match):
    return f'{match.group(1)}="{match.group(2)}"'.replace(" ", "")

def squish_value(html_code):
    # print(html_code)
    pattern = r'(\w+)="([^"]*)"'
    modified_html = re.sub(pattern, squish_space, html_code)
    return modified_html

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
        
