# import re

# string_data = 'class"why does this have a class"     love="hello"'

# # Define a pattern to match key-value pairs
# pattern = r'(\w+)="([^"]*)"'

# # Use re.findall to find all matches
# matches = re.findall(pattern, string_data)

# # Convert the matches into a dictionary
# result_dict = dict(matches)

# # Convert the dictionary items into a list of key-value pairs
# result_list = list(result_dict.items())

# print(result_list)


import re

html_code = '<div class="hello everyone"id="example">'

# Define a pattern to match spaces within the class attribute


def squish_spaces(match):
    # Replace spaces with an empty string within the matched group
    return match.group(0).replace(" ", "")

# Use re.sub with a custom function to modify the matched text



# import re

# html_code = '<div class="hello everyone"id="example"></div>'

# # Define a pattern to match spaces within the class attribute
# pattern = r'class="([^"]*)"(?=\sid|$)'

# def squish_spaces(match):
#     # Replace spaces with an empty string within the matched group
#     return match.group(0).replace(" ", "")

# # Use re.sub with a custom function to modify the matched text
# modified_html = re.sub(pattern, squish_spaces, html_code)

# print(modified_html)


# from bs4 import BeautifulSoup

# html = '<div class="hello everyone"id="example">'

# # Parse the HTML
# soup = BeautifulSoup(html, 'html.parser')

# # Find the <div> tag
# div_tag = soup.find('div')

# # Add a space between class and id attributes
# if 'class' in div_tag.attrs and 'id' in div_tag.attrs:
#     div_tag['class'] = f'{div_tag["class"][0]} {div_tag["id"]}'
#     del div_tag['id']

# # Get the modified HTML
# modified_html = str(soup)

# print(modified_html)


import re

# def get_attributes(html_tag):
#     # Define a regular expression pattern for attributes in an HTML tag
#     attribute_pattern = r'(\S+)\s*=\s*["\'](.*?)["\']'

#     # Find all attribute matches using re.findall
#     attribute_matches = re.findall(attribute_pattern, html_tag)

#     # Create a dictionary to store the attributes
#     attributes = {name: value for name, value in attribute_matches}

#     return attributes

# # Example usage
# html_tag = '<div class="example" id="myDiv" data-value="123">'

# # Call the function to get attributes
# attributes = get_attributes(html_tag)

# print(attributes)


import re

html_code = '<div class="hello everyone" id="example">'

# Define a pattern to match attribute values
pattern = r'(\w+)="([^"]*)"'

def squish_spaces(match):
    # Replace spaces with an empty string within the attribute value
    return f'{match.group(1)}="{match.group(2)}"'.replace(" ", "")

# Use re.sub with a custom function to modify all matched attributes
modified_html = re.sub(pattern, squish_spaces, html_code)

print(modified_html)