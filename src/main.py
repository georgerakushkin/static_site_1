from textnode import *
from copy_directory import copy_directory, generate_page, generate_pages_recursive
import os
import shutil



def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.makedirs("public")

    # Test directory copying
    try:
        copy_directory("static", "public")
        print("Successfully copied static directory to public")
    except Exception as e:
        print(f"Failed to copy directory: {e}")

    try:
        generate_pages_recursive(
            content_dir= "content",
            template_path="template.html",
            dest_dir= "public"
        )
        '''
        generate_page(
            from_path="content/index.md",
            template_path="template.html",
            dest_path="public/index.html"
        )
        '''
        print("Successfully generated index.html")
    except Exception as e:
        print(f"Failed to generate page: {e}")

if __name__ == "__main__":
    main()
