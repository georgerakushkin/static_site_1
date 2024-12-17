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

'''
TESTING
'''

if __name__ == "__main__":
    # Test markdown_to_blocks function
    test_markdown = """This is paragraph 1.

This is paragraph 2.

# This is a heading"""
    
    print("\nTesting markdown_to_blocks:")
    print("-" * 40)
    blocks = markdown_to_blocks(test_markdown)
    print("Input markdown:")
    print(test_markdown)
    print("\nOutput blocks:")
    for block in blocks:
        print(f"- {block}")

    # Test block_to_block_type function
    print("\nTesting block_to_block_type:")
    print("-" * 40)
    test_cases = [
        "# Heading",
        "Regular paragraph",
        "```code block```",
        "1. List item 1\n2. List item 2",
    ]
    
    for test in test_cases:
        block_type = block_to_block_type(test)
        print(f"\nInput: {test}")
        print(f"Block type: {block_type}")