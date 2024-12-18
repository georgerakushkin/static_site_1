def extract_title(markdown):
    count = 0;
    for char in markdown:
        if char == "#":
            count += 1;
        else:
            break
    if not markdown.startswith("#") or count!=1:
        print("Not correct header")
        raise Exception("Invalid header format")
    else:
        stripped_markdown = markdown.lstrip("#").strip()
        return stripped_markdown

if __name__ == "__main__":
    test_markdown_header = "# This is a header"

    print(extract_title(test_markdown_header))

