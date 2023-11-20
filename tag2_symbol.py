

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




# for k in range(len(available_tags_with_attribute)):
#     print(f"{available_tags_with_attribute[k]}")
# print(available_tags_with_attribute)


# # Read HTML code from a text file
# with open('./data/html_in_text.txt', 'r') as file:
#     html_code = file.read()

# # Specify the letter to replace HTML tags
# replacement_letter = 'H'  # Change this to your desired letter

# # Call the function to replace HTML tags
# modified_html = replace_html_tags_with_letter(html_code, replacement_letter,"html")

# # Print or save the modified HTML code
# print(modified_html)




def replace_tags_with_attribute(html_code, tag_name, attribute_name, replacement_letter):
    # Define a regular expression pattern to match the specified tag with the attribute
    pattern = re.compile(fr'<{tag_name}\s+{attribute_name}=".*?".*?>')

    # Replace the specified tags with the specified letter
    modified_html = re.sub(pattern, replacement_letter, html_code)

    return modified_html


def remove_content_tag(html_content):


    cleaned_html = re.sub(r'>[^<]+<', '><', html_content)

    # with open('cleanedtest.html', 'w') as file:
    #     file.write(cleaned_html)

    print(cleaned_html)
    return cleaned_html

# # Read HTML code from a text file
# with open('./data/html_in_text.txt', 'r') as file:
#     html_code = file.read()

# # Specify the tag name, attribute name, and the letter to replace the tags
# tag_name = 'html'  # Change this to your desired tag name
# attribute_name = 'lang'  # Change this to your desired attribute name
# replacement_letter = 'X'  # Change this to your desired letter

# # Call the function to replace tags with the specified attribute
# modified_html = replace_tags_with_attribute(html_code, tag_name, attribute_name, replacement_letter)

# # Print or save the modified HTML code
# print(modified_html)