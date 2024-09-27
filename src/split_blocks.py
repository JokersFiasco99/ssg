def markdown_to_blocks(markdown):
    # Split the markdown into blocks
    blocks = markdown.split("\n\n")
    # Remove any empty blocks or blocks with only whitespace
    return [block.strip() for block in blocks if block.strip()]

def block_to_block_type(block):
    # Check if the block is a heading
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    
    # Check if the block is a code block
    if block.startswith("```") and block.endswith("```"):
        return "code"
    
    # Check if the block is a quote
    if all(line.startswith(">") or line.strip() == "" for line in block.split("\n")):
        return "quote"
    
    # Check if the block is an unordered list
    if all(line.strip().startswith(("* ", "- ")) for line in block.split("\n")):
        return "unordered_list"
    
    # Check if the block is an ordered list
    lines = block.split("\n")
    if all(line.strip().split(". ", 1)[0].isdigit() for line in lines):
        numbers = [int(line.strip().split(". ", 1)[0]) for line in lines]
        if numbers[0] == 1 and all(numbers[i] == numbers[i-1] + 1 for i in range(1, len(numbers))):
            return "ordered_list"
    
    # If none of the above conditions are met, it's a paragraph
    return "paragraph"