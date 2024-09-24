from textnode import TextNode

# Define the text types
text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"

def split_nodes_delimiters(old_nodes):
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
                new_nodes.append(TextNode("", "text"))
                continue
            temp_nodes = [TextNode(text, 'text')]
            for delimiter, formatted_text_type in delimiters.items():
                new_temp_nodes = []
                for temp_node in temp_nodes:
                    if temp_node.text_type == 'text':
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
                        new_temp_nodes.append(temp_node)
                temp_nodes = new_temp_nodes
            new_nodes.extend(temp_nodes)
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == 'text':
            text = node.text
            parts = text.split("![")
            if len(parts) == 1:
                new_nodes.append(node)
                continue
            new_nodes.append(TextNode(parts[0], 'text'))
            for part in parts[1:]:
                closing_bracket = part.find(']')
                closing_paren = part.find(')')
                if closing_bracket != -1 and closing_paren != -1:
                    alt_text = part[:closing_bracket]
                    url = part[closing_bracket+2:closing_paren]
                    new_nodes.append(TextNode(alt_text, 'image', url))
                    if closing_paren + 1 < len(part):
                        new_nodes.append(TextNode(part[closing_paren+1:], 'text'))
                else:
                    new_nodes.append(TextNode("![" + part, 'text'))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == 'text':
            text = node.text
            parts = text.split("[")
            if len(parts) == 1:
                new_nodes.append(node)
                continue
            new_nodes.append(TextNode(parts[0], 'text'))
            for part in parts[1:]:
                closing_bracket = part.find(']')
                closing_paren = part.find(')')
                if closing_bracket != -1 and closing_paren != -1 and part[closing_bracket+1] == '(':
                    link_text = part[:closing_bracket]
                    url = part[closing_bracket+2:closing_paren]
                    new_nodes.append(TextNode(link_text, 'link', url))
                    if closing_paren + 1 < len(part):
                        new_nodes.append(TextNode(part[closing_paren+1:], 'text'))
                else:
                    new_nodes.append(TextNode("[" + part, 'text'))
        else:
            new_nodes.append(node)
    return new_nodes

