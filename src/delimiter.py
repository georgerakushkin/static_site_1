from textnode import *

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

#how can i isolate whats inside two delimiters?

'''
Now, let's think about a slightly more complex scenario. What if we had multiple delimited sections?

text = "one*two*three*four*five"
parts = text.split("*")
Copy icon
Can you predict what parts would look like? And here's the tricky part - how would you know which parts were meant to be delimited and which weren't?

Here's a hint: when you split with a delimiter, the even-indexed items (0, 2, 4...) will be outside the delimiters, and the odd-indexed items (1, 3, 5...) will be inside.

Would this pattern be useful for your split_nodes_delimiter function?
'''
