from htmlnode import LeafNode

# TextNode: Building block for text with styling
class TextNode:
    # Constructor for TextNode
    def __init__(self, text, text_type, url=None):
        self.text = text  # The actual text content
        self.text_type = text_type  # The type of text (e.g., bold, italic, link)
        self.url = url  # URL for links or images, None for other types
    
    # Equality comparison for TextNode
    def __eq__(self, other):
        # Compare all attributes of two TextNodes
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False

    # String representation of TextNode
    def __repr__(self):
        # Return a string representation of the TextNode
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

# Convert TextNode to HTMLNode
def text_node_to_html_node(text_node):
    # Plain text: No special formatting
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    # Bold text: Wrap in <b> tag
    elif text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    # Italic text: Wrap in <i> tag
    elif text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    # Code text: Wrap in <code> tag
    elif text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    # Link text: Create <a> tag with href
    elif text_node.text_type == "link":
        if text_node.url is None:
            raise ValueError("URL for a link-type TextNode cannot be None")
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    # Image: Create <img> tag with src and alt
    elif text_node.text_type == "image":
        if text_node.url is None:
            raise ValueError("URL for an image-type TextNode cannot be None")
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    # Invalid text type: Raise an error
    else:
        raise ValueError(f"Invalid text type: {text_node.text_type}")

def text_to_text_nodes(text):
    # Import necessary splitting functions
    from split_nodes import split_nodes_delimiters, split_nodes_image, split_nodes_link
    
    # Create initial TextNode with the entire text
    initial_node = TextNode(text, "text")

    # Split the text into image nodes
    image_nodes = split_nodes_image([initial_node])

    # Further split into image and link nodes
    image_and_link_nodes = split_nodes_link(image_nodes)

    # Finally, split based on delimiters (bold, italic, code)
    final_nodes = split_nodes_delimiters(image_and_link_nodes)

    # Return the fully processed list of TextNodes
    return final_nodes