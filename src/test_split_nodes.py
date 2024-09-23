import unittest
from split_nodes import split_nodes_delimiters
from textnode import TextNode

class TestSplitNodesDelimiters(unittest.TestCase):

    def test_single_bold_delimiter(self):
        old_nodes = [TextNode("This is **bold** text", "text")]
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text")
        ]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_single_italic_delimiter(self):
        old_nodes = [TextNode("This is *italic* text", "text")]
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text")
        ]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_single_code_delimiter(self):
        old_nodes = [TextNode("This is `code` text", "text")]
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("code", "code"),
            TextNode(" text", "text")
        ]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_multiple_delimiters(self):
        old_nodes = [TextNode("This is **bold** and *italic* and `code` text", "text")]
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" and ", "text"),
            TextNode("italic", "italic"),
            TextNode(" and ", "text"),
            TextNode("code", "code"),
            TextNode(" text", "text")
        ]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_no_delimiters(self):
        old_nodes = [TextNode("This is plain text", "text")]
        expected_nodes = [TextNode("This is plain text", "text")]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_empty_text(self):
        old_nodes = [TextNode("", "text")]
        expected_nodes = [TextNode("", "text")]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

if __name__ == '__main__':
    unittest.main()