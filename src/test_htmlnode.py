import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

# Test suite for HTMLNode and its subclasses
class TestHTMLNode(unittest.TestCase):
    # Test HTMLNode props_to_html method
    def test_props_to_html(self):
        # Create an HTMLNode with properties
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "id": "hello"}
        )
        # Assert that the props_to_html method returns the correct string
        self.assertEqual(node.props_to_html(), 'class="greeting" id="hello"')

    # Test LeafNode to_html method
    def test_leaf_node_to_html(self):
        # Create a LeafNode with a tag, text, and property
        node = LeafNode("p", "Hello, world!", {"class": "greeting"})
        # Assert that the to_html method returns the correct HTML string
        self.assertEqual(node.to_html(), '<p class="greeting">Hello, world!</p>')

    # Test ParentNode to_html method
    def test_parent_node_to_html(self):
        # Create child nodes
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode("i", "Italic text")
        # Create a ParentNode with children and a property
        parent = ParentNode("p", [child1, child2], {"class": "content"})
        expected = '<p class="content"><b>Bold text</b><i>Italic text</i></p>'
        # Assert that the to_html method returns the correct HTML string
        self.assertEqual(parent.to_html(), expected)

    # Test HTMLNode with no tag
    def test_html_node_no_tag(self):
        # Create a LeafNode with no tag
        node = LeafNode(None, "Just some text")
        # Assert that the to_html method returns just the text
        self.assertEqual(node.to_html(), "Just some text")

    # Test HTMLNode with no children or value
    def test_html_node_no_children_or_value(self):
        # Create a LeafNode with an empty string as value
        node = LeafNode("br", "")
        # Assert that the to_html method returns a self-closing tag
        self.assertEqual(node.to_html(), "<br></br>")

# Run tests if script is executed directly
if __name__ == "__main__":
    unittest.main()