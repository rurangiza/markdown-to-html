"""
TextNode Class:
an intermediate representation of text
based on markdown and soon to be converted to HTML
"""

from htmlnode import LeafNode

class TextNode:
    def __init__(self, text: str, text_type: str, url: str=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: 'TextNode'):
        return self.text == other.text \
            and self.text_type == other.text_type \
            and self.url == other.url
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

    
def text_node_to_html_node(node: TextNode) -> LeafNode:
    match node.text_type:
        case 'text':
            return LeafNode(None, node.text, None)
        case 'bold':
            return LeafNode('b', node.text, None)
        case 'italic':
            return LeafNode('i', node.text, None)
        case 'code':
            return LeafNode('code', node.text, None)
        case 'image':
            return LeafNode('img', None, {
                'src': node.url,
                'alt': node.text,
            })
        case _:
            raise ValueError('not valid text node')