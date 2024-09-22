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
    def text_node_to_html_node(self):
        # 🅱️ Bold text
        if self.text_type == "bold":
            return LeafNode("b", self.text)
        # 🖋️ Italic text
        elif self.text_type == "italic":
            return LeafNode("i", self.text)
        # 💻 Code text
        elif self.text_type == "code":
            return LeafNode("code", self.text)
        # 🔗 Link text
        elif self.text_type == "link":
            if self.url is None:
                raise ValueError("URL for a link-type TextNode cannot be None")
            return LeafNode("a", props={"href": self.url})
        # 🖼️ Image
        elif self.text_type == "image":
            if self.url is None:
                raise ValueError("URL for an image-type TextNode cannot be None")
            return LeafNode("img", props={"src": self.url})
        # ❌ Invalid text type
        else:
            raise ValueError(f"Invalid text type: {self.text_type}")