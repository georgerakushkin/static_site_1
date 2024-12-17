from textnode import *
import re

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)] #create a textnode with the text provided and default text type
    nodes = split_nodes_image(nodes) #split the nodes based on if theres an image in the text
    nodes = split_nodes_link(nodes) #split the nodes based on if theres a link in the text
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD) #split the nodes based on if theres a bold delimiter in the text
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC) #split the nodes based on if theres an italic delimiter in the text
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE) #split the nodes based on if theres a code delimiter in the text   
    return nodes


def split_nodes_delimiter(old_nodes, delimiter,text_type): #splits the nodes based on the delimiter and text type   
    new_list_of_nodes = [] #creates a new list to store nodes
    for node in old_nodes: #for every node in the old_nodes list
        if node.text_type != TextType.TEXT: #if the node text_type is not text, append it to the new list of nodes
            new_list_of_nodes.append(node) #append the node to the new list of nodes
            continue #continue to the next node

        split_node_text = node.text.split(delimiter)#split the node text where the delimiter is found
        for i, part in enumerate(split_node_text): #for every i and part in the enumerated split_node_text list
            if i%2 != 0: #if i is not even, meaning that the part is the delimited part
                _text_type = text_type #set the text type to the text type passed in
            else: #if i is even, meaning that the part is not the delimited part
                _text_type = TextType.TEXT #set the text type to text
            new_list_of_nodes.append(TextNode(part, _text_type)) 
    return new_list_of_nodes

def split_nodes_image(old_nodes): #splits the nodes based on if theres an image in the text
    new_nodes = []
    for node in old_nodes:
        if len(extract_markdown_images(node.text)) == 0:
            new_nodes.append(node)
        else:
            remaining_text = node.text  # Start with full text
            images = extract_markdown_images(node.text)
            for img_alt, img_url in images:
                sections = remaining_text.split(f"![{img_alt}]({img_url})", 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_url))
                remaining_text = sections[1] if len(sections) > 1 else ""
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if len(extract_markdown_links(node.text)) == 0:
            new_nodes.append(node)
        else:
            remaining_text = node.text
            links = extract_markdown_links(node.text)
            for link_text, link_url in links:
                sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                remaining_text = sections[1] if len(sections) > 1 else ""
            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

