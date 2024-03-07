import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_empty_eq(self):
        node1 = HTMLNode()
        node2 = HTMLNode()
        self.assertEqual(node1.props_to_html(), node2.props_to_html())

    def test_filled_eq(self):
        node1 = HTMLNode('p', 'hello, world', None, {'class': 'highlight'})
        node2 = HTMLNode('p', 'hello, world', None, {'class': 'highlight'})
        self.assertEqual(node1.__repr__(), node2.__repr__())
    
    def test_filled_noteq(self):
        node1 = HTMLNode('p', 'hello, world', None, {'class': 'high'})
        node2 = HTMLNode('p', 'hello, world', None, {'class': 'light'})
        self.assertNotEqual(node1.__repr__(), node2.__repr__())
    
    def test_single_noteq(self):
        node1 = HTMLNode('button', None, None, {'class': 'btn'})
        node2 = HTMLNode('button', None, None, None)
        self.assertNotEqual(node1.props_to_html(), node2.props_to_html())

class TestLeafNode(unittest.TestCase):

    def test_leaf_empty(self):
        node1 = LeafNode('h1', 'nothing special')
        node2 = LeafNode('h1', 'nothing special')
        self.assertEqual(node1, node2)

    def test_basic(self):
        a = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(a.to_html(), '<p>This is a paragraph of text.</p>')

    def test_with_attribute(self):
        a = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(a.to_html(), '<a href="https://www.google.com">Click me!</a>')


class TestParentNode(unittest.TestCase):
    def test_basic(self):
        node = ParentNode(
            'p',
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        ans = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), ans)
    
    def test_basic(self):
        node = ParentNode(
            'p',
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        ans = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), ans)

if __name__ == '__main__':
    unittest.main()