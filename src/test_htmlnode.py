import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html1(self):
        node = HTMLNode("p", "value", props = {"a": "b", "hallo": "ja"})
        self.assertEqual(node.props_to_html(),' a="b" hallo="ja"')

    def test_props_to_html2(self):
        node = HTMLNode(value = "", props = {})
        self.assertEqual(node.props_to_html(),'')

    def test_props_to_html3(self):
        node = HTMLNode(value = "", props = {"a": "b"})
        self.assertEqual(node.props_to_html(),' a="b"')

if __name__ == "__main__":
    unittest.main()