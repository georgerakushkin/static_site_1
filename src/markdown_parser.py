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
    filtered_blocks = markdown_to_blocks(markdown) #turns the markdown into a list of lines/blocks
    print("Blocks:", filtered_blocks)  # Debug print
    #print("Filtered blocks:", filtered_blocks)  # Debug print
    
    div_node = ParentNode("div", "", []) #main node that gets everything put into it
    
    for block in filtered_blocks: #for each line/block
        type_of_block = block_to_block_type(block)
        #print(f"Block type: {type_of_block}")  # Debug print
        #print(f"Block content: {block}")       # Debug print
        match type_of_block:
            case "paragraph":
                paragraph_node = LeafNode("p", block)
                div_node.children.append(paragraph_node)
            case "quote":
                quote_node = LeafNode("blockquote", block[1:].strip())
                div_node.children.append(quote_node)
            case "unordered_list":
                items = [line.lstrip('* ').lstrip("- ") for line in block.split("\n")]

                ul_node = ParentNode("ul", "", [])

                for item in items:
                    li_node = LeafNode("li", item)
                    ul_node.children.append(li_node)
                
                div_node.children.append(ul_node)
            case "ordered_list":
                items = [line.lstrip(f'{i+1}. ') for i, line in enumerate(block.split("\n"))]

                ol_node = ParentNode("ol", "", [])

                for item in items:
                    li_node = LeafNode("li", item)
                    ol_node.children.append(li_node)
                
                div_node.children.append(ol_node)
            case "code":
                items = [line.strip("```") for line in block.split("\n")]

                outer_node = ParentNode("pre", "", [])

                for item in items:
                    pre_node = LeafNode("code", item)
                    outer_node.children.append(pre_node)
                div_node.children.append(outer_node)
            case "heading":
                og_len = len(block)
                stripped_block = block.lstrip("#")
                number_of_hashes = og_len - len(stripped_block)
                heading_node = LeafNode(f"h{number_of_hashes}", stripped_block.strip())
                div_node.children.append(heading_node)



    
    #print("Final div node:", div_node)  # Debug print
    return div_node
            

            