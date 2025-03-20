import unittest
from textnode import TextNode, TextType
from node_utils import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is `code` inside text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" inside text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_no_split(self):
        node = TextNode("This has no delimiter", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]
        self.assertEqual(result, expected)

    def test_multiple_splits(self):
        node = TextNode("`code1` and `code2`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("", TextType.TEXT),
            TextNode("code1", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("code2", TextType.CODE),
            TextNode("", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_non_text_node(self):
        node = TextNode("Bold text", TextType.BOLD)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]
        self.assertEqual(result, expected)

    def test_different_delimiter(self):
        node = TextNode("This is ~italic~ text", TextType.TEXT)
        result = split_nodes_delimiter([node], "~", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [node]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()