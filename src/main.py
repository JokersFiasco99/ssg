import re
import os
import shutil
from block_to_html import markdown_to_html_node

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

def copy_directory(src, dst):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dst):
        os.makedirs(dst)
    
    # Walk through the source directory
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            # If it's a directory, recursively copy it
            copy_directory(s, d)
        else:
            # If it's a file, copy it
            shutil.copy2(s, d)
        print(f"Copied: {s} -> {d}")

# Function to extract title from Markdown text
def extract_title(markdown):
    # Regular expression pattern to match h1 header
    pattern = r"^#\s*(.+)$"
    match = re.search(pattern, markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()
    else:
        raise Exception("No h1 header found in the markdown file")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown file
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    
    # Read the template file
    with open(template_path, 'r') as file:
        template_content = file.read()
    
    # Convert markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    # Extract title
    title = extract_title(markdown_content)
    
    # Replace placeholders in the template
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Write the full HTML to the destination file
    with open(dest_path, 'w') as file:
        file.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith('.md'):
                # Construct the full path for the markdown file
                md_file_path = os.path.join(root, file)
                
                # Construct the relative path from the content directory
                rel_path = os.path.relpath(md_file_path, dir_path_content)
                
                # Construct the destination path, replacing .md with .html
                dest_file_path = os.path.join(dest_dir_path, os.path.splitext(rel_path)[0] + '.html')
                
                # Generate the page
                generate_page(md_file_path, template_path, dest_file_path)
                print(f"Generated {dest_file_path} successfully.")

# Main entry point of the application
def main():
    # Delete anything in the public directory
    if os.path.exists("public"):
        shutil.rmtree("public")
    
    # Copy static directory to public
    copy_directory("static", "public")
    print("Static directory copied to public successfully.")
    
    # Generate pages recursively
    generate_pages_recursive("content", "template.html", "public")
    print("Generated all pages successfully.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()