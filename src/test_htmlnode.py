import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(tag='div', props={'class': 'container', 'id': 'main'})
        self.assertEqual(node.props_to_html(), ' class="container" id="main"')

    def test_repr(self):
        node = HTMLNode(tag='div', props={'class': 'container', 'id': 'main'})
        self.assertEqual(repr(node), "HTMLNode(tag=div, value=None, children=None, props={'class': 'container', 'id': 'main'})")
    
    def test_props_to_html_none(self):
        node = HTMLNode(tag='div')
        self.assertEqual(node.props_to_html(), None)

    def test_to_html_leaf_node(self):
        node = LeafNode(tag='div', value='Hello, World!')
        self.assertEqual(node.to_html(), '<div>Hello, World!</div>')

    def test_to_html_leaf_node_no_tag(self):
        node = LeafNode(tag='div', value='Hello, World!', props={'class': 'container', 'id': 'main'})
        self.assertEqual(node.to_html(), '<div class="container" id="main">Hello, World!</div>')

if __name__ == "__main__":
    unittest.main()