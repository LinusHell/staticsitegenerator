from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "plain text"
    BOLD = "bold"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"


class TextNode():


    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text= text
        self.text_type = text_type
        self.url = url
        if self.text_type == "IMAGE" and self.url is None:
                raise Exception("Image without URL")
        if self.text_type == "LINK" and self.url is None:
                    raise Exception("Link without URL")

    def __eq__(self, other):
        return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type.name:
        case 'TEXT':
            return LeafNode(None, text_node.text)
        case 'BOLD':
            return LeafNode("b", text_node.text)
        case 'ITALIC':
            return LeafNode("i", text_node.text)
        case 'CODE':
            return LeafNode("code", text_node.text)
        case 'LINK':
            return LeafNode("a", text_node.text, {"href": text_node.url}) # type: ignore comment
        case 'IMAGE':
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text}) # type: ignore comment
        case _:
            raise ValueError("TextNode has non defined TextType.")

