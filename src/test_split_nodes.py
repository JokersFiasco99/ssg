import unittest
from split_nodes import split_nodes_delimiters, split_nodes_link, split_nodes_image
from textnode import TextNode

# Test suite for split_nodes_delimiters function
class TestSplitNodesDelimiters(unittest.TestCase):

    def test_single_bold_delimiter(self):
        # Test case for a single bold delimiter
        old_nodes = [TextNode("This is **bold** text", "text")]
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" text", "text")
        ]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_single_italic_delimiter(self):
        # Test case for a single italic delimiter
        old_nodes = [TextNode("This is *italic* text", "text")]
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text")
        ]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_single_code_delimiter(self):
        # Test case for a single code delimiter
        old_nodes = [TextNode("This is `code` text", "text")]
        expected_nodes = [
            TextNode("This is ", "text"),
            TextNode("code", "code"),
            TextNode(" text", "text")
        ]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_multiple_delimiters(self):
        # Test case for multiple delimiters in a single node
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
        # Test case for text without any delimiters
        old_nodes = [TextNode("This is plain text", "text")]
        expected_nodes = [TextNode("This is plain text", "text")]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

    def test_empty_text(self):
        # Test case for an empty text node
        old_nodes = [TextNode("", "text")]
        expected_nodes = [TextNode("", "text")]
        self.assertEqual(split_nodes_delimiters(old_nodes), expected_nodes)

# Test suite for split_nodes_link and split_nodes_image functions
class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_link(self):
        # Test case for a single link in text
        node = TextNode("This is a [link](https://example.com) in text.", "text")
        result = split_nodes_link([node])
        expected = [
            TextNode("This is a ", "text"),
            TextNode("link", "link", "https://example.com"),
            TextNode(" in text.", "text")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_multiple(self):
        # Test case for multiple links in text
        node = TextNode("Text with [link1](https://example1.com) and [link2](https://example2.com)", "text")
        result = split_nodes_link([node])
        expected = [
            TextNode("Text with ", "text"),
            TextNode("link1", "link", "https://example1.com"),
            TextNode(" and ", "text"),
            TextNode("link2", "link", "https://example2.com")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_link_no_links(self):
        # Test case for text without any links
        node = TextNode("This is text without any links.", "text")
        result = split_nodes_link([node])
        self.assertEqual(result, [node])

    def test_split_nodes_image(self):
        # Test case for a single image in text
        node = TextNode("This is an ![image](https://example.com/image.jpg) in text.", "text")
        result = split_nodes_image([node])
        expected = [
            TextNode("This is an ", "text"),
            TextNode("image", "image", "https://example.com/image.jpg"),
            TextNode(" in text.", "text")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_multiple(self):
        # Test case for multiple images in text
        node = TextNode("Text with ![img1](https://example1.com/img1.jpg) and ![img2](https://example2.com/img2.jpg)", "text")
        result = split_nodes_image([node])
        expected = [
            TextNode("Text with ", "text"),
            TextNode("img1", "image", "https://example1.com/img1.jpg"),
            TextNode(" and ", "text"),
            TextNode("img2", "image", "https://example2.com/img2.jpg")
        ]
        self.assertEqual(result, expected)

    def test_split_nodes_image_no_images(self):
        # Test case for text without any images
        node = TextNode("This is text without any images.", "text")
        result = split_nodes_image([node])
        self.assertEqual(result, [node])

if __name__ == '__main__':
    unittest.main()