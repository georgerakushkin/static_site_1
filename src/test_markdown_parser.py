import unittest
from markdown_parser import markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestMarkdownParser(unittest.TestCase):
    def test_markdown_to_html_node(self):
        # Test a simple paragraph
        node = markdown_to_html_node("This is a paragraph")
        self.assertEqual(node.tag, "div")  # parent should be a div
        self.assertEqual(len(node.children), 1)  # should have one child
        self.assertEqual(node.children[0].tag, "p")  # child should be a paragraph
        
        # Test a heading
        node = markdown_to_html_node("# Heading")
        self.assertEqual(node.children[0].tag, "h1")
        
        # Test multiple blocks
        markdown = """
# Heading
This is a paragraph
"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(len(node.children), 2)  # should have two blocks

        # Test paragraph block type
        markdown = "This is a regular paragraph."
        node = markdown_to_html_node(markdown)
        self.assertEqual(node.tag, "div")  # Check root node
        self.assertEqual(len(node.children), 1)  # Should have one paragraph child
        self.assertEqual(node.children[0].tag, "p")  # Child should be paragraph
        self.assertEqual(node.children[0].value, "This is a regular paragraph.")  # Check content

        # Test multiple paragraphs
        markdown = """This is paragraph one.

This is paragraph two."""
        node = markdown_to_html_node(markdown)
        self.assertEqual(len(node.children), 2)  # Should have 2 paragraph children
        self.assertEqual(node.children[0].tag, "p")
        self.assertEqual(node.children[0].value, "This is paragraph one.")
        self.assertEqual(node.children[1].tag, "p") 
        self.assertEqual(node.children[1].value, "This is paragraph two.")

    def test_manual_cases(self):
        # Your manual test cases from __main__ block
        test_markdown = """This is a paragraph..."""
        html_node = markdown_to_html_node(test_markdown)
        # Add assertions here instead of prints

if __name__ == "__main__":
    unittest.main()