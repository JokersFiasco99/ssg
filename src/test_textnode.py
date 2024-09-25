import unittest
from textnode import TextNode, text_node_to_html_node, text_to_text_nodes

# Test suite for TextNode
class TestTextNode(unittest.TestCase):
    # Test TextNode initialization
    def test_init(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "bold")

    # Test TextNode equality
    def test_eq(self):
        node1 = TextNode("Hello", "bold")
        node2 = TextNode("Hello", "bold")
        node3 = TextNode("Hello", "italic")
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

    # Test TextNode representation
    def test_repr(self):
        node = TextNode("Hello", "bold")
        self.assertEqual(repr(node), "TextNode(Hello, bold, None)")

    # Test conversion from TextNode to HTMLNode
    def test_text_node_to_html_node(self):
        node = TextNode("Hello", "bold")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.value, "Hello")
        self.assertEqual(html_node.tag, "b")

    # Test invalid text type conversion
    def test_text_node_to_html_node_invalid_text_type(self):
        node = TextNode("Hello", "invalid")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    # Test link conversion with None URL
    def test_text_node_to_html_node_link_with_none_url(self):
        node = TextNode("Hello", "link")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    # Test text_to_text_nodes function
    def test_text_to_text_nodes(self):
        # Test plain text
        text = "Hello, world!"
        nodes = text_to_text_nodes(text)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Hello, world!")
        self.assertEqual(nodes[0].text_type, "text")

        # Test bold text
        text = "Hello, **bold** world!"
        nodes = text_to_text_nodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello, ")
        self.assertEqual(nodes[0].text_type, "text")
        self.assertEqual(nodes[1].text, "bold")
        self.assertEqual(nodes[1].text_type, "bold")
        self.assertEqual(nodes[2].text, " world!")
        self.assertEqual(nodes[2].text_type, "text")

        # Test italic text
        text = "Hello, *italic* world!"
        nodes = text_to_text_nodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello, ")
        self.assertEqual(nodes[0].text_type, "text")
        self.assertEqual(nodes[1].text, "italic")
        self.assertEqual(nodes[1].text_type, "italic")
        self.assertEqual(nodes[2].text, " world!")
        self.assertEqual(nodes[2].text_type, "text")

        # Test code text
        text = "Hello, `code` world!"
        nodes = text_to_text_nodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello, ")
        self.assertEqual(nodes[0].text_type, "text")
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[1].text_type, "code")
        self.assertEqual(nodes[2].text, " world!")
        self.assertEqual(nodes[2].text_type, "text")

        # Test link
        text = "Hello, [link](https://example.com) world!"
        nodes = text_to_text_nodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello, ")
        self.assertEqual(nodes[0].text_type, "text")
        self.assertEqual(nodes[1].text, "link")
        self.assertEqual(nodes[1].text_type, "link")
        self.assertEqual(nodes[1].url, "https://example.com")
        self.assertEqual(nodes[2].text, " world!")
        self.assertEqual(nodes[2].text_type, "text")

        # Test image
        text = "Hello, ![image](https://example.com/image.jpg) world!"
        nodes = text_to_text_nodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello, ")
        self.assertEqual(nodes[0].text_type, "text")
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].text_type, "image")
        self.assertEqual(nodes[1].url, "https://example.com/image.jpg")
        self.assertEqual(nodes[2].text, " world!")
        self.assertEqual(nodes[2].text_type, "text")

        # Test combined elements
        text = "**Bold** and *italic* and `code` and [link](https://example.com) and ![image](https://example.com/image.jpg)"
        nodes = text_to_text_nodes(text)
        self.assertEqual(len(nodes), 9)
        self.assertEqual(nodes[0].text_type, "bold")
        self.assertEqual(nodes[1].text_type, "text")
        self.assertEqual(nodes[2].text_type, "italic")
        self.assertEqual(nodes[3].text_type, "text")
        self.assertEqual(nodes[4].text_type, "code")
        self.assertEqual(nodes[5].text_type, "text")
        self.assertEqual(nodes[6].text_type, "link")
        self.assertEqual(nodes[7].text_type, "text")
        self.assertEqual(nodes[8].text_type, "image")

# Run the tests if this script is executed
if __name__ == "__main__":
    unittest.main()