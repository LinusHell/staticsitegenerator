import unittest
from markdown2htmlnode import markdown_to_html_node



class Testmarkdown_to_html_node(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_headingblock(self):
        md = """
# **Heading**

## Heading 2

### Heading 3
    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1><b>Heading</b></h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
        )

    def test_ulistblock(self):
            md = """
- Item one
- Item two with _italic_
        """
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><ul><li>Item one</li><li>Item two with <i>italic</i></li></ul></div>",
            )

    def test_olistblock(self):
            md = """
1. Item one
2. Item two with _italic_
        """
            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><ol><li>Item one</li><li>Item two with <i>italic</i></li></ol></div>",
            )
    def test_quoteblock(self):
                md = """
> This is a quote
> that spans multiple lines
            """
                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(
                    html,
                    "<div><blockquote>This is a quote that spans multiple lines</blockquote></div>",
                )

       
if __name__ == "__main__":
    unittest.main()