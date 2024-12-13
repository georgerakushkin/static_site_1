# Static Site Generator

A Python-based static site generator that converts markdown to HTML, with support for various text formatting options.

## Project Structure


## Core Components

### 1. Text Processing (textnode.py)
- Defines `TextNode` class for representing text with different formatting types
- Supports multiple text types through `TextType` enum:
  - Normal text
  - Bold
  - Italic
  - Code
  - Links
  - Images
  - Plain text

### 2. HTML Generation (htmlnode.py)
- `HTMLNode`: Base class for HTML element generation
- Two types of nodes:
  - `LeafNode`: For elements without children (e.g., `<p>text</p>`)
  - `ParentNode`: For elements with children (e.g., `<div><p>text</p></div>`)
- Includes property handling for HTML attributes

### 3. Delimiter Processing (delimiter.py)
- Functions for parsing markdown syntax:
  - `split_nodes_delimiter()`: Splits text based on delimiters
  - `extract_markdown_images()`: Extracts image syntax (`![alt](url)`)
  - `extract_markdown_links()`: Extracts link syntax (`[text](url)`)

### 4. Testing
- Unit tests implemented for TextNode functionality
- Test runner available via `test.sh`

## Current Features
- Text node equality comparison
- HTML generation with nested elements
- Markdown parsing for links and images
- CSS styling support
- Property handling for HTML elements

## Running the Project
- Execute main program: `./main.sh`
- Run tests: `./test.sh`

## Development Status
The project appears to be in active development with core functionality for:
- Text processing
- HTML generation
- Markdown parsing

Next steps might include:
- Complete markdown to HTML conversion
- More extensive test coverage
- Documentation improvements
- Additional markdown features support