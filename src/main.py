import re

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches























# 🚀 Main entry point of the application
def main():
    # TODO: Implement main logic
    pass

# 🏁 Run the main function if this script is executed
if __name__ == "__main__":
    main()