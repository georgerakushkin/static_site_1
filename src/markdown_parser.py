from htmlnode import *
from markdown_blocks import *


'''
    BLOCK_TYPES:
    paragraph
    quote, 
    code, 
    heading,
    ordered list, 
    unordered list
'''

def markdown_to_html_node(markdown):
    filtered_blocks = markdown_to_blocks(markdown)
    print("markdown" + markdown + "end")
    #print("Filtered blocks:", filtered_blocks)  # Debug print
    
    div_node = ParentNode("div", "", [])
    
    for block in filtered_blocks:
        type_of_block = block_to_block_type(block)
        #print(f"Block type: {type_of_block}")  # Debug print
        #print(f"Block content: {block}")       # Debug print
        match type_of_block:
            case "paragraph":
                paragraph_node = LeafNode("p", block)
                div_node.children.append(paragraph_node)
    
    #print("Final div node:", div_node)  # Debug print
    return div_node
            
if __name__ == "__main__":
    # Test markdown string
    test_markdown = """This is a paragraph.

This is another paragraph with some **bold** text."""

    # Convert markdown to HTML node
    html_node = markdown_to_html_node(test_markdown)
    
    # Print the result
    print("\nTest Results:")
    print("Input Markdown:")
    print("-" * 40)
    print(test_markdown)
    print("-" * 40)
    print("\nOutput HTML Node:")
    print("-" * 40)
    print(markdown_to_html_node(test_markdown))
    print("-" * 40)
            