class HTMLNode:
    # 🏗️ Base class for all HTML nodes
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # 🚀 Convert node to HTML (implemented in subclasses)
    def to_html(self):
        raise NotImplementedError("to_html method must be implemented in subclass")
    
    # 🔧 Convert props to HTML string
    def props_to_html(self):
        if self.props:
            return ''.join([f' {key}="{value}"' for key, value in self.props.items()])
        return None
    
    # 📝 String representation of the node
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    # 🍃 Base class for all leaf nodes
    def __init__(self, value, tag="div", props=None):
        super().__init__(tag, value, None, props)
    
    # 🎨 Generate HTML for leaf node
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        props_html = self.props_to_html()
        props_str = props_html if props_html is not None else ''
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"