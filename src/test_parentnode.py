import unittest
from leafnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_two_children(self):
        child_node = LeafNode("b", "child1")
        child_node2 = LeafNode("a", "child2", {"key": "value"})
        parent_node = ParentNode("div", [child_node,child_node2])
        self.assertEqual(
            parent_node.to_html(),
            '<div><b>child1</b><a key="value">child2</a></div>',
        )

    def test_to_html_no_children(self):
        parent_node = ParentNode("p", [])
        self.assertEqual(
            parent_node.to_html(), "<p></p>"
        )

    def test_to_html_nested(self):
        child1 = LeafNode("i", "child1")
        child2 = LeafNode(None, "child2")
        parent_second_level = ParentNode("p",[child1])
        parent_third_level = ParentNode("b", [child2, parent_second_level])
        self.assertEqual(
            parent_third_level.to_html(),
            "<b>child2<p><i>child1</i></p></b>"
        )
        




if __name__ == "__main__":
    unittest.main()