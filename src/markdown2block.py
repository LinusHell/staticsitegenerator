from enum import Enum

def markdown_to_blocks(markdown: str) -> list[str]:
    result: list[str] = []
    split_list: list[str] = markdown.split("\n\n")
    for string in split_list:
        cleaned_string = string.strip()
        if cleaned_string != "":
            result.append(cleaned_string)
    return result


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def block_to_block_type(block: str) -> BlockType:
    if (block.startswith("# ") or
        block.startswith("## ") or
        block.startswith("### ") or
        block.startswith("#### ") or
        block.startswith("##### ") or
        block.startswith("###### ")
        ):
        return BlockType.HEADING
    if block.startswith("```\n")  and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        split_block = block.split("\n")
        is_quote = True
        for line in split_block:
            if not line.startswith(">"):
                is_quote = False
        if is_quote:
            return BlockType.QUOTE
    if block.startswith("- "):
        split_block = block.split("\n")
        is_unordlist = True
        for line in split_block:
            if not line.startswith("- "):
                is_unordlist = False
        if is_unordlist:
            return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        split_block = block.split("\n")
        is_ordlist = True
        i=1
        for line in split_block:
            if not line.startswith(f"{i}. "):
                is_ordlist = False
            i += 1
        if is_ordlist:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
        
    