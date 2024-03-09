import unittest
from textnode import TextNode
from textnode import text_node_to_html_node, split_nodes_delimiter

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode('hello', 'bold')
        node2 = TextNode('world', 'bold')
        self.assertNotEqual(node, node2)

class TestConverter(unittest.TestCase):

    def test_eq(self):
        text_node = TextNode('This is bold', 'bold', None)
        result = text_node_to_html_node(text_node)
        expected = '<b>This is bold</b>'
        self.assertEqual(result.to_html(), expected)
    
    def test_noteq(self):
        text_node = TextNode('This is bold', 'italic', None)
        result = text_node_to_html_node(text_node)
        expected = '<b>This is bold</b>'
        self.assertNotEqual(result.to_html(), expected)
    
    def test_empty(self):
        result = ""
        try:
            text_node = TextNode(None, None, None)
            result = text_node_to_html_node(text_node).to_html()
        except ValueError as v:
            result = v
        except Exception as e:
            result = e
        expected = 'ValueError: not valid text node'
        self.assertNotEqual(result, expected)

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic(self):
        node = TextNode("This is text with a `code block` word", 'p')
        lists = split_nodes_delimiter([node], "`", 'p')

        # turn List[List[TextNode]] to a string for checking
        result = ""
        for list in lists:
            for item in list:
                result += str(item)

        expected = 'TextNode(This is text with a , p, None)TextNode(code block, code, None)TextNode( word, p, None)'
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()