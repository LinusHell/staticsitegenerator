from htmlnode import HTMLNode
from markdown2block import markdown_to_blocks, block_to_block_type, BlockType
from mark2text import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode


def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks: list[str] = markdown_to_blocks(markdown)
    blocks_as_htmlnode: list[HTMLNode] = []
    for block in blocks:
        blocks_as_htmlnode.append(block_to_htmlnode(block))
    return ParentNode("div",  blocks_as_htmlnode)
    


def block_to_htmlnode(block: str) -> HTMLNode: #or should this be a list of TextNodes?
    block_type = block_to_block_type(block)
    match block_type:
        case BlockType.CODE:
            return ParentNode("pre",[LeafNode("code",block[4:-3])])
        case BlockType.HEADING:
            return heading_to_HTML(block)
        case BlockType.QUOTE:
            return quote_to_HTML(block)
        case BlockType.UNORDERED_LIST:
            return unord_to_HTML(block)
        case BlockType.ORDERED_LIST:
            return ord_to_HTML(block)
        case BlockType.PARAGRAPH:
            return paragraph_to_HTML(block)
        case _: 
            raise ValueError("Invalid Blocktype in block_to_htmlnode")


def text_to_children(text: str) -> list[HTMLNode]:
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]

def heading_to_HTML(block: str) -> HTMLNode:
    return ParentNode(f"h{len(block.split(" ",1)[0])}",text_to_children(block.split(" ",1)[1]))

def quote_to_HTML(block: str) -> HTMLNode:
    childrens = []
    lines = [(line.lstrip() + " ") for line in block[1:].split("\n>")]
    lines[-1] = lines[-1][:-1]
    for i in range(len(lines)):
        if lines[i][0] == " ":
            childrens.extend(text_to_children(lines[i][1:]))
        else:
            childrens.extend(text_to_children(lines[i]))
    return ParentNode("blockquote",childrens)

def unord_to_HTML(block: str) -> HTMLNode:
    childrens = []
    lines = block[2:].split("\n- ")
    for i in range(len(lines)):
        childrens.append(ParentNode("li",text_to_children(lines[i])))
    return ParentNode("ul",childrens)

def ord_to_HTML(block: str) -> HTMLNode:
    childrens = []
    lines = block.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ",1)[1]
        childrens.append(ParentNode("li",text_to_children(lines[i])))
    return ParentNode("ol",childrens)

def paragraph_to_HTML(block: str) -> HTMLNode:
    modified_block = " ".join([line.strip() for line in block.split("\n")])
    return ParentNode("p",text_to_children(modified_block))


