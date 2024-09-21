import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    # 🧪 Test TextNode initialization
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

    # 🧬 Test TextNode representation
    def test_repr(self):
        node = TextNode("Hello", "bold")
        self.assertEqual(repr(node), "TextNode(Hello, bold)")

# 🏁 Run the tests if this script is executed
if __name__ == "__main__":
    unittest.main()