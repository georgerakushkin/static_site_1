import re
from htmlnode import *

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block =="":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(markdown):
    block_type = "paragraph"
    count = 1
    if bool(re.match(r"^#{1,6} .+", markdown.strip())):
        block_type = "heading"
    elif markdown.startswith("```"):
        if markdown.endswith("```"):
            block_type = "code"
    elif markdown.startswith(">"):
        for line in markdown.split("\n"):
            if not line.startswith(">"):
                return "paragraph"
        block_type = "quote"
    elif markdown.startswith("* "):
        for line in markdown.split("\n"):
            if not (line.startswith("- ")) and not (line.startswith("* ")):
                return "paragraph"   
        block_type = "unordered_list"       
    elif markdown.startswith("- "):
        for line in markdown.split("\n"):
            if not (line.startswith("- ")) and not (line.startswith("* ")):
                return"paragraph"   
        block_type = "unordered_list"     
    elif markdown.startswith("1. "):
        blocks = markdown.split("\n")
        for line in blocks:
            if line.startswith(f"{count}. "):
                count += 1
                block_type = "ordered_list"
            else:
                block_type = "paragraph"
    return block_type

