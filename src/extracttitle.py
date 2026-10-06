from markdown2block import markdown_to_blocks

def extract_title(markdown: str) -> str:
    for block in markdown_to_blocks(markdown):
        if block.startswith("# "):
            return block.split("# ",1)[1].strip()
    raise Exception("Markdown has no Title in extract_title.")
