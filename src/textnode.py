from htmlnode import LeafNode

# 🧱 TextNode: Building block for text with styling
class TextNode:
    # 🏗️ Constructor for TextNode
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    # 🔍 Equality comparison for TextNode
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    # 📝 String representation of TextNode
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

# 🔄 Convert TextNode to HTMLNode
def text_node_to_html_node(text_node):
    # 📝 Plain text
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    # 🅱️ Bold text
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    # 🖋️ Italic text
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    # 💻 Code text
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    # 🔗 Link text
    elif text_node.text_type == "link":
        if text_node.url is None:
            raise ValueError("URL for a link-type TextNode cannot be None")
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    # 🖼️ Image
    elif text_node.text_type == "image":
        if text_node.url is None:
            raise ValueError("URL for an image-type TextNode cannot be None")
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    # ❌ Invalid text type
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")