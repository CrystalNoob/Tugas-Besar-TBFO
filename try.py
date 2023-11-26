# import re

# # # def extract_tag_info(html_tag):
# # #     html_tag = html_tag.strip()
# # #     if html_tag.startswith("<!--") and html_tag.endswith("-->"):
# # #         return ['CMT']

# # #     # Pattern to match tag name and attributes
# # #     tag_pattern = r'^<(\w+)(.*?)>$'
# # #     attr_pattern = r'(\w+)=["\'](.*?)["\']'

# # #     tag_match = re.match(tag_pattern, html_tag)
# # #     if tag_match:
# # #         tag_name = tag_match.group(1)
# # #         attributes_string = tag_match.group(2)
        
# # #         attributes = re.findall(attr_pattern, attributes_string)
# # #         result = [tag_name]
        
# # #         for attr_name, attr_value in attributes:
# # #             result.extend([attr_name, '=', attr_value])

# # #         return result

# # #     return []

# # # # Example usage
# # # # html_tag = '<input type="text" name="user_name" value>'
# # # # print(extract_tag_info(html_tag))

# # from bs4 import BeautifulSoup

# # # Your HTML content
# # html_content = """
# # <html>
# # <head>
# #     <title>Sample Page</title>
# # </head>
# # <body>
# #     <div class="content">
# #         <p class="important" id="first-paragraph">This is an important paragraph.</p>
# #         <p class="normal">This is a normal paragraph.</p>
# #     </div>
# # </body>
# # </html>
# # """

# # # Create a BeautifulSoup object
# # soup = BeautifulSoup(html_content, 'html.parser')

# # # Find elements by class name
# # class_elements = soup.find_all()  # Find all elements with class="important"

# # for element in class_elements:
# #     print(f"Class name: {element['class']}")
# #     print(f"Attribute 'id': {element.get('id')}")
# #     print("--------")


# # example_string = 'This is an="example" with="equal=signs" inside="double=quotes".'

# # # Regex pattern


# # # Function to replace equals signs
# # def replace_equals(match):
# #     return match.group(0).replace('=', 'X')  # Replace '=' with 'X'

# # # Perform the substitution
# # result_string = re.sub(pattern, replace_equals, example_string)

# # # Print the result
# # print(result_string)

# import re

# # Example string
# example_string = 'This is an="example" with="equal=signs" inside="double=quotes".'

# # Regex pattern
# pattern = r'="([^"]*)"'

# # Function to replace equals signs
# def replace_equals(match):
#     return match.group(0).replace('=', 'X')  # Replace '=' with 'X'

# # Perform the substitution
# result_string = re.sub(pattern, replace_equals, example_string)

# # Print the result
# print(result_string)


import re

# Example string
example_string = 'This is an"example" with="equal=signs" outside="double=quotes".'

# Regex pattern
pattern = r'="([^"]*)"'

# Function to replace equals signs
def replace_equals(match):
    inside_quotes = match.group(1)
    replaced_inside_quotes = inside_quotes.replace('=', 'X')
    return f'="{replaced_inside_quotes}"'

# Perform the substitution
result_string = re.sub(pattern, replace_equals, example_string)

# Print the result
print(result_string)