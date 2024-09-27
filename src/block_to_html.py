from split_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode
from textnode import TextNode, text_to_text_nodes, text_node_to_html_node

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown):
    # Split the markdown into blocks
    blocks = markdown_to_blocks(markdown)
    # Create a parent HTMLNode (div)
    parent_node = HTMLNode("div")
    # Loop over each block
    for block in blocks:
        # Convert the block to a block type
        block_type = block_to_block_type(block)
        # Convert the block to an HTMLNode
        block_node = create_block_node(block_type, block)
        # Add the block node to the parent node
        parent_node.add_child(block_node)
    # Return the parent node
    return parent_node

def create_block_node(block_type, block):
    if block_type == "heading":
        level = len(block.split()[0])  # Count the number of '#'
        content = block.lstrip('#').strip()
        return HTMLNode(f"h{level}", None, text_to_children(content))
    elif block_type == "code":
        # Remove the ``` at the start and end
        content = block.strip('`').strip()
        code_node = HTMLNode("code", None, [TextNode(content)])
        return HTMLNode("pre", None, [code_node])
    elif block_type == "quote":
        # Remove the '>' from each line
        content = '\n'.join(line.lstrip('>').strip() for line in block.split('\n'))
        return HTMLNode("blockquote", None, text_to_children(content))
    elif block_type == "unordered_list":
        items = block.split('\n')
        li_nodes = [HTMLNode("li", None, text_to_children(item.lstrip('*-').strip())) for item in items]
        return HTMLNode("ul", None, li_nodes)
    elif block_type == "ordered_list":
        items = block.split('\n')
        li_nodes = [HTMLNode("li", None, text_to_children(item.split('.', 1)[1].strip())) for item in items]
        return HTMLNode("ol", None, li_nodes)
    else:
        return HTMLNode("p", None, text_to_children(block))
