import re

def normalize_html_tag(tag):
    # Replace multiple spaces with a single space
    tag = re.sub(r'\s+', ' ', tag)
    # Ensure no space before and one space after '=' in attributes
    tag = re.sub(r'\s*=\s*', '=', tag)
    return tag

html_string = "<p class = " "   ></p>, <div id=        \"\"></div>"

html_string = re.sub(r'<[^>]+>', lambda match: normalize_html_tag(match.group()), html_string)
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


# available_tags = ["html","head","body","title", "h1","h2","h3","h4","h5","h6","p","em","b","abbr","strong","small","div","table","tr","td","th","br","hr","link","script","a","img","button","form","input"]
# symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'v', 'w', 'x', 'y',"$","%","@","r",'s', "",'t','u', ""]

dictionary = {'html': 'a', 'head': 'b', 'body': 'c', 'title': 'd', 'h1': 'e', 'h2': 'f', 'h3': 'g', 'h4': 'h', 
            'h5': 'i', 'h6': 'j', 'p': 'k', 'em': 'l', 'b': 'm', 'abbr': 'n', 'strong': 'o', 'small': 'p', 'div': 'q', 
            'table': 'v', 'tr': 'w', 'td': 'x', 'th': 'y', 'br': '$', 'hr': '%', 'link': '@', 'script': 'r', 'a': 's', 
            'img': '#', 'button': 't', 'form': 'u', 'input': '^'}

# tag_symbol_dict = dict(zip(available_tags, symbols))

# print(tag_symbol_dict)


