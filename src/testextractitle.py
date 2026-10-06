import unittest
from extracttitle import extract_title

class TestParentNode(unittest.TestCase):
    def test_extracttitle(self):
        md = """

# This is the title


> This is not.
"""
        self.assertEqual(extract_title(md), "This is the title")


    def test_notitle(self):
        md = """

This has no title

> This is not.
    """
        with self.assertRaises(Exception):
            extract_title(md)

    def test_twotitle(self):
        md = """
# This is the title

# This is not.
        """
        self.assertEqual(extract_title(md), "This is the title")


    
        




if __name__ == "__main__":
    unittest.main()