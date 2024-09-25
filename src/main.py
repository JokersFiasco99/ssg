import re

# Function to extract image information from Markdown text
def extract_markdown_images(text):
    # Regular expression pattern to match Markdown image syntax
    pattern = r"!\[(.*?)\]\((.*?)\)"
    # Find all matches in the text
    matches = re.findall(pattern, text)
    return matches

# Function to extract link information from Markdown text
def extract_markdown_links(text):
    # Regular expression pattern to match Markdown link syntax
    # The negative lookbehind (?<!) ensures we don't match image syntax
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    # Find all matches in the text
    matches = re.findall(pattern, text)
    return matches

# Main entry point of the application
def main():
    # TODO: Implement main logic
    pass

# Run the main function if this script is executed
if __name__ == "__main__":
    main()