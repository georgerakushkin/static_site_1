from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"
    TEXT = "text"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
                return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node):
     if not isinstance(text_node, TextNode):
          raise Exception("not a TextNode")
     match text_node.text_type:
          case TextType.NORMAL:
               return text_node.text
          case TextType.BOLD:
               return f"<b>{text_node.text}</b>"
          case TextType.ITALIC:
               return f"<i>{text_node.text}</i>"
          case TextType.CODE:
               return f"<code>{text_node.text}</code>"
          case TextType.LINKS:
               return f"<a href='{text_node.url}'>{text_node.text}</a>"
          case TextType.IMAGES:
               return f"<img src='{text_node.url}' alt='{text_node.text}'>"
          case TextType.TEXT:
               return text_node.text
          case _:
               raise Exception(f"Invalid text type: {text_node.text_type}")



