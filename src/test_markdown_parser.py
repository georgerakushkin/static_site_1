from markdown_parser import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

def test_markdown_to_html_node():
    # Test a simple paragraph
    node = markdown_to_html_node("This is a paragraph")
    assert node.tag == "div"  # parent should be a div
    assert len(node.children) == 1  # should have one child
    assert node.children[0].tag == "p"  # child should be a paragraph
    
    # Test a heading
    node = markdown_to_html_node("# Heading")
    assert node.children[0].tag == "h1"
    
    # Test multiple blocks
    markdown = """
# Heading
This is a paragraph
"""
    node = markdown_to_html_node(markdown)
    assert len(node.children) == 2  # should have two blocks

    # Test paragraph block type
    markdown = "This is a regular paragraph."
    node = markdown_to_html_node(markdown)
    assert node.tag == "div"  # Check root node
    assert len(node.children) == 1  # Should have one paragraph child
    assert node.children[0].tag == "p"  # Child should be paragraph
    assert node.children[0].value == "This is a regular paragraph."  # Check content

    # Test multiple paragraphs
    markdown = """
This is paragraph one.

This is paragraph two.
"""
    node = markdown_to_html_node(markdown)
    assert len(node.children) == 2  # Should have two paragraph children
    assert node.children[0].tag == "p"
    assert node.children[1].tag == "p"
    assert node.children[0].value == "This is paragraph one."
    assert node.children[1].value == "This is paragraph two."