import unittest
from textnode import TextType, TextNode
from mark2text import text_to_textnodes, split_nodes_link, split_nodes_image, split_nodes_delimiter, extract_markdown_links, extract_markdown_images

class Test_mark2text(unittest.TestCase):
    def test_split_notes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_split_notes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold block", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_split_notes_delimiter_italic(self):
        node = TextNode("This is text with an _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic block", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_split_notes_delimiter_nontext(self):
        node = TextNode("This is text with an _italic block_ word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes,
            [node]
        )

    def test_split_notes_delimiter_twonodes(self):
        node = TextNode("**bold** and more", TextType.TEXT)
        node2 = TextNode("Nothing to do", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(new_nodes,
                    [
                        TextNode("bold",TextType.BOLD),
                        TextNode(" and more",TextType.TEXT),
                        node2
                    ]
                )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is text with an [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_link_nolink(self):
        matches = extract_markdown_links(
            "This is text without an link [to boot dev]https://www.boot.dev)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_noimages(self):
        matches = extract_markdown_images(
            "This is text without image !image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_2images(self):
        matches = extract_markdown_images(
            "This is text with ![image2](https://i.imgur.com/zjjcJKZ.png) an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image2", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_image_in_image(self):
            matches = extract_markdown_images(
                "This is text with an ![image](![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([("image", "![image](https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_link_does_not_extract_image(self):
            matches = extract_markdown_links(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
            )
            self.assertListEqual([], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.LINK, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_onlylink(self):
            node = TextNode(
                "[image](https://i.imgur.com/zjjcJKZ.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    
                    TextNode("image", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                
                ],
                new_nodes,
            )

    def test_split_no_link(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                
                TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
            
            ],
            new_nodes,
        )

    def test_split_no_image(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                
                TextNode("[image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
            
            ],
            new_nodes,
        )

    def test_mixed_markdown(self):
        self.assertEqual(
            text_to_textnodes(
                "A **bold** _italic_ `snippet` "
                "![map](https://example.com/map.png) "
                "[docs](https://example.com)"
            ),
            [
                TextNode("A ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" ", TextType.TEXT),
                TextNode("snippet", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("map", TextType.IMAGE, "https://example.com/map.png"),
                TextNode(" ", TextType.TEXT),
                TextNode("docs", TextType.LINK, "https://example.com"),
            ],
        )

if __name__ == "__main__":
    unittest.main()
