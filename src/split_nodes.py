from textnode import TextNode

# Define the text types
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"

# Split nodes based on delimiters (**, *, `)
def split_nodes_delimiters(old_nodes):
    # Define delimiters and their corresponding text types
    delimiters = {
        '**': 'bold',
        '*': 'italic',
        '`': 'code'
    }
    
    new_nodes = []
    for node in old_nodes:
        if node.text_type == 'text':
            text = node.text
            if text == "":
                # Handle empty text nodes
                new_nodes.append(TextNode("", "text"))
                continue
            temp_nodes = [TextNode(text, 'text')]
            for delimiter, formatted_text_type in delimiters.items():
                new_temp_nodes = []
                for temp_node in temp_nodes:
                    if temp_node.text_type == 'text':
                        # Split the text by the current delimiter
                        parts = temp_node.text.split(delimiter)
                        for i, part in enumerate(parts):
                            if part or i % 2 == 1:
                                if i % 2 == 0:
                                    # Text outside the delimiters
                                    new_temp_nodes.append(TextNode(part, 'text'))
                                else:
                                    # Text inside the delimiters
                                    new_temp_nodes.append(TextNode(part, formatted_text_type))
                    else:
                        # Keep non-text nodes as they are
                        new_temp_nodes.append(temp_node)
                temp_nodes = new_temp_nodes
            new_nodes.extend(temp_nodes)
        else:
            # Keep non-text nodes as they are
            new_nodes.append(node)
    return new_nodes

# Split nodes for images
def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == 'text':
            text = node.text
            # Split the text by image markdown syntax
            parts = text.split("![")
            if len(parts) == 1:
                # No image syntax found, keep the node as is
                new_nodes.append(node)
                continue
            # Add the text before the first image syntax
            new_nodes.append(TextNode(parts[0], 'text'))
            for part in parts[1:]:
                closing_bracket = part.find(']')
                closing_paren = part.find(')')
                if closing_bracket != -1 and closing_paren != -1:
                    # Extract alt text and URL
                    alt_text = part[:closing_bracket]
                    url = part[closing_bracket+2:closing_paren]
                    # Create image node
                    new_nodes.append(TextNode(alt_text, 'image', url))
                    if closing_paren + 1 < len(part):
                        # Add remaining text after the image syntax
                        new_nodes.append(TextNode(part[closing_paren+1:], 'text'))
                else:
                    # Invalid image syntax, treat as normal text
                    new_nodes.append(TextNode("![" + part, 'text'))
        else:
            # Keep non-text nodes as they are
            new_nodes.append(node)
    return new_nodes

# Split nodes for links
def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == 'text':
            text = node.text
            # Split the text by link markdown syntax
            parts = text.split("[")
            if len(parts) == 1:
                # No link syntax found, keep the node as is
                new_nodes.append(node)
                continue
            # Add the text before the first link syntax
            new_nodes.append(TextNode(parts[0], 'text'))
            for part in parts[1:]:
                closing_bracket = part.find(']')
                closing_paren = part.find(')')
                if closing_bracket != -1 and closing_paren != -1 and part[closing_bracket+1] == '(':
                    # Extract link text and URL
                    link_text = part[:closing_bracket]
                    url = part[closing_bracket+2:closing_paren]
                    # Create link node
                    new_nodes.append(TextNode(link_text, 'link', url))
                    if closing_paren + 1 < len(part):
                        # Add remaining text after the link syntax
                        new_nodes.append(TextNode(part[closing_paren+1:], 'text'))
                else:
                    # Invalid link syntax, treat as normal text
                    new_nodes.append(TextNode("[" + part, 'text'))
        else:
            # Keep non-text nodes as they are
            new_nodes.append(node)
    return new_nodes

