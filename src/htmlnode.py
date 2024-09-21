class HTMLNode:
    # base class for all HTML nodes
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # abstract method to convert node to HTML will be implemented in subclasses
    def to_html(self):
        raise NotImplementedError("to_html method must be implemented in subclass")
    
    # method to convert props to HTML
    def props_to_html(self):
        if self.props:
            return ''.join([f' {key}="{value}"' for key, value in self.props.items()])
        return None
    
    # method to represent node as a string
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    # base class for all leaf nodes
    def __init__(self, value, tag="div", props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        props_html = self.props_to_html()
        props_str = props_html if props_html is not None else ''
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"