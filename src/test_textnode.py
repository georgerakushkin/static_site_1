import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_nodes_with_italic_type(self):
        node3 = TextNode("test1", TextType.ITALIC)
        node4 = TextNode("test1", TextType.ITALIC)
        self.assertEqual(node3, node4)
    def test_eq_nodes_with_same_href(self):
        node5 = TextNode("test1", TextType.BOLD, "www.google.com")
        node6 = TextNode("test1", TextType.BOLD, "www.google.com")
        self.assertEqual(node5, node6)
    def test_neq_different_text(self):
        node1 = TextNode("test1", TextType.BOLD)
        node2 = TextNode("test2", TextType.BOLD)
        self.assertNotEqual(node1, node2)     
    def test_neq_different_type(self):
        node1 = TextNode("test1", TextType.BOLD)
        node2 = TextNode("test1", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
if __name__ == "__main__":
    unittest.main()