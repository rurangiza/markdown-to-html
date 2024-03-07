import unittest
from htmlnode import HTMLNode

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

if __name__ == '__main__':
    unittest.main()