# 🌳 HTMLNode: Base class for HTML elements
class HTMLNode:
    # 🏗️ Constructor for HTMLNode
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children or []
        self.props = props or {}

    # 📝 String representation of HTMLNode
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {len(self.children)}, props: {self.props})"

    # 🔧 Generate props string for HTML
    def props_to_html(self):
        if not self.props:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    # 🏭 Generate HTML string
    def to_html(self):
        if self.tag is None:
            return self.value or ""
        
        props = self.props_to_html()
        props = " " + props if props else ""
        
        if self.children:
            children_html = "".join(child.to_html() for child in self.children)
            return f"<{self.tag}{props}>{children_html}</{self.tag}>"
        elif self.value:
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{props}></{self.tag}>"

# 🔗 LeafNode: HTMLNode without children
class LeafNode(HTMLNode):
    # 🏗️ Constructor for LeafNode
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    # 📝 String representation of LeafNode
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, props: {self.props})"

# 🧱 ParentNode: HTMLNode with children
class ParentNode(HTMLNode):
    # 🏗️ Constructor for ParentNode
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    # 📝 String representation of ParentNode
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {len(self.children)}, props: {self.props})"