from textnode import *
from copy_directory import copy_directory

print("hello world")

def main():
    obj_textnode = TextNode("text here", TextType.BOLD, "https://www.boot.dev")
    print (obj_textnode)

    # Test directory copying
    try:
        copy_directory("static", "public")
        print("Successfully copied static directory to public")
    except Exception as e:
        print(f"Failed to copy directory: {e}")

if __name__ == "__main__":
    main()
