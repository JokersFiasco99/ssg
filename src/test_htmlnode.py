import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

# 🧪 Test suite for HTMLNode and its subclasses
class TestHTMLNode(unittest.TestCase):
    # ✅ Test HTMLNode props_to_html method
    def test_props_to_html(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "id": "hello"}
        )
        self.assertEqual(node.props_to_html(), 'class="greeting" id="hello"')

    # 🍃 Test LeafNode to_html method
    def test_leaf_node_to_html(self):
        node = LeafNode("p", "Hello, world!", {"class": "greeting"})
        self.assertEqual(node.to_html(), '<p class="greeting">Hello, world!</p>')

    # 👨‍👩‍👧‍👦 Test ParentNode to_html method
    def test_parent_node_to_html(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode("i", "Italic text")
        parent = ParentNode("p", [child1, child2], {"class": "content"})
        expected = '<p class="content"><b>Bold text</b><i>Italic text</i></p>'
        self.assertEqual(parent.to_html(), expected)

    # 🏷️ Test HTMLNode with no tag
    def test_html_node_no_tag(self):
        node = HTMLNode(value="Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    # 🚫 Test HTMLNode with no children or value
    def test_html_node_no_children_or_value(self):
        node = HTMLNode("br")
        self.assertEqual(node.to_html(), "<br></br>")

# 🏃‍♂️ Run tests if script is executed directly
if __name__ == "__main__":
    unittest.main()