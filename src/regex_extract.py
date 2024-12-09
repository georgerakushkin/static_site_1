import re

def extract_markdown_images(text):
    list_of_tuples = []
    alt_text = re.findall(r"\[(.*?)\]", text)
    url = re.findall(r"\((.*?)\)", text)


    #url = re.findall(r"https://\w+\.\w+")
'''
# images
r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

# regular links
r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"





'''