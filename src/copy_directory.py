import os
import shutil
import logging
from markdown_parser import markdown_to_html_node
from extract_title import extract_title

def copy_directory(src_dir: str, dst_dir: str):
    try:
        if not os.path.exists(src_dir):
            raise FileNotFoundError(f"source directory '{src_dir}' does not exist")
        
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            dst_path = os.path.join(dst_dir, item)

            try:
                if os.path.isdir(src_path):
                    copy_directory(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
            except Exception as e:
                logging.error(f"Failed to copy {src_path}: {str(e)}")
    except Exception as e:
        logging.error(f"Directory copy failed: {str(e)}")
        raise

def generate_page(from_path, template_path, dest_path):
    
    # Create the destination directory if it doesn't exist
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r", encoding="utf-8") as file:
        content = file.read()
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()
    html_string = markdown_to_html_node(content).to_html()
    page_title = extract_title(content)

    final_html = template.replace("{{ Title}}", page_title).replace("{{ Content }}", html_string)

    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(final_html)

def generate_pages_recursive(content_dir, template_path, dest_dir):
    # Make sure destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # List all items in content directory
    for item in os.listdir(content_dir):
        src_path = os.path.join(content_dir, item)
        
        # If it's a directory, recurse into it
        if os.path.isdir(src_path):
            # Create corresponding directory in destination
            new_dest_dir = os.path.join(dest_dir, item)
            generate_pages_recursive(src_path, template_path, new_dest_dir)
        
        # If it's a markdown file, convert it
        elif item.lower().endswith(('.md', '.markdown')):
            # Create HTML file path with same structure
            html_filename = os.path.splitext(item)[0] + '.html'
            dest_path = os.path.join(dest_dir, html_filename)
            
            # Generate the HTML page
            generate_page(src_path, template_path, dest_path)
'''
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for path in dir_path_content:
        if path.lower().endswith(('.md', '.markdown')):
            with open(path, "r", encoding= "utf-8") as file:
                content = file.read()
            with open(template_path, "r", encoding= "utf-8") as file:
                template = file.read()
            html_string = markdown_to_html_node(content).to_html()
            page_title = extract_title(content)
            final_html = template.replace("{{ Title}}", page_title).replace("{{ Content }}", html_string)

            with open(dest_dir_path, "w", encoding="utf-8") as file:
                file.write(final_html)
'''



