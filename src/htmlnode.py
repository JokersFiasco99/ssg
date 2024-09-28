# Base class for HTML nodes
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        # Initialize HTML node with optional tag, value, children, and properties
        self.tag = tag
        self.value = value
        self.children = children or []  # Default to empty list if no children provided
        self.props = props or {}  # Default to empty dict if no properties provided

    def props_to_html(self):
        # Convert properties dictionary to HTML attribute string
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def to_html(self):
        # Abstract method to be implemented by subclasses
        raise NotImplementedError("to_html method must be implemented in subclasses")

    def add_child(self, child):
        # Add a child node to this node
        self.children.append(child)

# Class for leaf nodes (nodes without children)
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Initialize leaf node with tag, value, and optional properties
        super().__init__(tag, value, None, props)

    def to_html(self):
        # Convert leaf node to HTML string
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return self.value  # Return raw value if no tag is specified
        props = self.props_to_html()
        props = " " + props if props else ""  # Add space before props if they exist
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"

# Class for parent nodes (nodes with children)
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        # Initialize parent node with tag, children, and optional properties
        super().__init__(tag, None, children, props)

    def to_html(self):
        # Convert parent node and its children to HTML string
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have at least one child")
        
        props = self.props_to_html()
        props = " " + props if props else ""  # Add space before props if they exist
        children_html = "".join(child.to_html() for child in self.children)  # Recursively convert children to HTML
        return f"<{self.tag}{props}>{children_html}</{self.tag}>"
