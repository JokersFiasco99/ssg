import unittest
from textnode import TextNode

# 🧪 Test suite for TextNode
class TestTextNode(unittest.TestCase):
    # 🏗️ Test TextNode initialization
    def test_init(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.text, "This is a text node")
        self.assertEqual(node.text_type, "bold")

    # 🔍 Test TextNode equality
    def test_eq(self):
        node1 = TextNode("Hello", "bold")
        node2 = TextNode("Hello", "bold")
        node3 = TextNode("Hello", "italic")
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

    # 🖨️ Test TextNode representation
    def test_repr(self):
        node = TextNode("Hello", "bold")
        self.assertNotEqual(repr(node), "TextNode(Hello, bold)")

    # 🔄 Test conversion from TextNode to HTMLNode
    def test_text_node_to_html_node(self):
        node = TextNode("Hello", "bold")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.value, "Hello")
        self.assertEqual(html_node.tag, "b")

    # ❌ Test invalid text type conversion
    def test_text_node_to_html_node_invalid_text_type(self):
        node = TextNode("Hello", "invalid")
        with self.assertRaises(Exception):
            node.text_node_to_html_node()

    # 🔗 Test link conversion with None URL
    def test_text_node_to_html_node_link_with_none_url(self):
        node = TextNode("Hello", "link")
        with self.assertRaises(ValueError):
            node.text_node_to_html_node()

# 🏁 Run the tests if this script is executed
if __name__ == "__main__":
    unittest.main()