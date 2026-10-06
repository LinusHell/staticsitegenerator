import unittest
from markdown2block import markdown_to_blocks, block_to_block_type, BlockType

class TestParentNode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
        [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ],
    )

    def test_markdown_to_blocks_no_blocks(self):
                md = """
    
    
    
    
    
                """
                blocks = markdown_to_blocks(md)
                self.assertEqual(
                blocks,
                [
                    
                ],
            )

    def test_markdown_to_blocks_one_block(self):
        md = """

One block



        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
        blocks,
        [
            "One block"
        ],
    )

    def test_block_to_block_type_HEAD(self):
        md = "# a"
        self.assertEqual(block_to_block_type(md),BlockType.HEADING)

    def test_block_to_block_type_HEAD2(self):
            md = "## "
            self.assertEqual(block_to_block_type(md),BlockType.HEADING)

    def test_block_to_block_type_HEAD3(self):
                md = "###### #"
                self.assertEqual(block_to_block_type(md),BlockType.HEADING)

    def test_block_to_block_type_noHEAD(self):
                    md = "#."
                    self.assertEqual(block_to_block_type(md),BlockType.PARAGRAPH)

    def test_block_to_block_type_CODE(self):
            md = "```\na```"
            self.assertEqual(block_to_block_type(md),BlockType.CODE)

    def test_block_to_block_type_noCODE(self):
                md = "```n ```"
                self.assertEqual(block_to_block_type(md),BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        md = ">a\n>>"
        self.assertEqual(block_to_block_type(md),BlockType.QUOTE)

    def test_block_to_block_type_noquote(self):
            md = ">a\n >"
            self.assertEqual(block_to_block_type(md),BlockType.PARAGRAPH)

    def test_block_to_block_type_unord(self):
        md = "- a \n- "
        self.assertEqual(block_to_block_type(md),BlockType.UNORDERED_LIST)

    def test_block_to_block_type_nunord(self):
            md = "- a \n-"
            self.assertEqual(block_to_block_type(md),BlockType.PARAGRAPH)

    def test_block_to_block_type_ord(self):
        md = "1. \n2. a"
        self.assertEqual(block_to_block_type(md),BlockType.ORDERED_LIST)

    def test_block_to_block_type_nord(self):
        md = "1. \n2.a"
        self.assertEqual(block_to_block_type(md),BlockType.PARAGRAPH)

    def test_block_to_block_type_nord2(self):
            md = "1. \n3.a"
            self.assertEqual(block_to_block_type(md),BlockType.PARAGRAPH)
    

    


if __name__ == "__main__":
    unittest.main()