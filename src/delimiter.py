from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter,text_type):
    new_list_of_nodes = [] #where text type nodes in the input list are split based on syntax
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_list_of_nodes.append(node)
            continue

        split_node_text = node.text.split(delimiter)#list of text thats been split
        for i, part in enumerate(split_node_text):
            if i%2 != 0:
                _text_type = text_type
            else:
                _text_type = TextType.TEXT
            new_list_of_nodes.append(TextNode(part, _text_type)) 
    return new_list_of_nodes

def split_nodes_image(old_nodes):
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

