import unittest
from block_to_html import markdown_to_html_node, create_block_node
from htmlnode import HTMLNode

class TestBlockToHTML(unittest.TestCase):
    def test_create_block_node_heading(self):
        block = "# Heading 1"
        node = create_block_node("heading", block)
        self.assertEqual(node.tag, "h1")
        self.assertEqual(node.children[0].value, "Heading 1")

    def test_create_block_node_unordered_list(self):
        block = "* Item 1\n* Item 2"
        node = create_block_node("unordered_list", block)
        self.assertEqual(node.tag, "ul")
        self.assertEqual(len(node.children), 2)
        self.assertEqual(node.children[0].tag, "li")
        self.assertEqual(node.children[1].tag, "li")

    def test_create_block_node_ordered_list(self):
        block = "1. First item\n2. Second item"
        node = create_block_node("ordered_list", block)
        self.assertEqual(node.tag, "ol")
        self.assertEqual(len(node.children), 2)
        self.assertEqual(node.children[0].tag, "li")
        self.assertEqual(node.children[1].tag, "li")

    def test_create_block_node_paragraph(self):
        block = "This is a simple paragraph."
        node = create_block_node("paragraph", block)
        self.assertEqual(node.tag, "p")
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].value, "This is a simple paragraph.")

if __name__ == '__main__':
    unittest.main()