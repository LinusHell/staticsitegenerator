from textnode import TextType, TextNode
import re

def split_nodes_delimiter(
        old_nodes: list[TextNode], 
        delimiter: str,
        text_type: TextType
        ) -> list[TextNode]:             
        new_nodes: list[TextNode] = []
        for node in old_nodes:
                if node.text_type != TextType.TEXT:
                     new_nodes.append(node)
                     continue
                split_node_list = node.text.split(delimiter)
                if len(split_node_list) % 2 != 1:
                    raise Exception("TextNode has non-closed delimiter"
                    " in split_nodes_delimiter.")
                for i in range(len(split_node_list)):
                    inclosed = bool(i % 2)
                    if split_node_list[i] != "":
                        if inclosed == True:
                            new_nodes.append(TextNode(split_node_list[i],text_type))
                        else:
                             new_nodes.append(TextNode(split_node_list[i],TextType.TEXT))
        return new_nodes
        
                    
def extract_markdown_images(text: str) -> list[(str,)]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text: str) -> list[(str,)]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)",text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or node.text == "":
             new_nodes.append(node)
             continue
        images: list[(str,)] = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for (image,url) in images:
             split_text = remaining_text.split(f"![{image}]({url})",1)
             if len(split_text) != 2:
                raise Exception("Text can't be split at image in split_nodes_image")
             remaining_text = split_text[1]
             if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0],TextType.TEXT))
             new_nodes.append(TextNode(image,TextType.IMAGE,url))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return new_nodes



def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or node.text == "":
            new_nodes.append(node)
            continue
        links: list[(str,)] = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for (link,url) in links:
            split_text = remaining_text.split(f"[{link}]({url})",1)
            if len(split_text) != 2:
                raise Exception("Text can't be split at link in split_nodes_link")
            remaining_text = split_text[1]
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0],TextType.TEXT))
            new_nodes.append(TextNode(link,TextType.LINK,url))
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,TextType.TEXT))
    return new_nodes

def text_to_textnodes(text: str) -> list[TextNode]:
    result = [TextNode(text, TextType.TEXT)]
    result = split_nodes_delimiter(result, "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
        
    return result