"""
TextNode Class:
an intermediate representation of text
based on markdown and soon to be converted to HTML
"""

from htmlnode import LeafNode
from typing import List, Tuple
import re

class TextNode:
    def __init__(self, text: str, text_type: str, url: str=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other: 'TextNode') -> bool:
        return self.text == other.text \
            and self.text_type == other.text_type \
            and self.url == other.url
    
    def __repr__(self) -> str:
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
        case 'link':
            return LeafNode('a', node.text, {
                'href': node.url
            })
        case 'image':
            return LeafNode('img', "", {
                'src': node.url,
                'alt': node.text,
            })
        case _:
            raise ValueError('not valid text node')

def split_nodes_delimiter( old_nodes: str, delimiter: str, text_type: str) -> List[List[TextNode]]:
    new_nodes = []

    def get_md_type(syntax: str) -> str:
        match syntax:
            case '`':
                return 'code'
            case '*':
                return 'italic'
            case '**':
                return 'bold'
            case _:
                return 'text'

    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
            continue
        if node.text.count(delimiter) != 2:
            raise SyntaxError('Invalid markdown: odd number of delimiter symbol')
        curr = []
        tokens = node.text.split(delimiter)
        for token in tokens:
            if len(token) == 0:
                continue
            if f' {delimiter}{token}' in node.text:
                curr.append(TextNode(
                    token.lstrip(delimiter), get_md_type(delimiter))
                )
            else:
                curr.append(TextNode(token, text_type))
        new_nodes.append(curr)

    return new_nodes

def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: List[TextNode]):  
    final = []

    for node in old_nodes:

        result = []
        text = node.text
        default_type = node.text_type
        images = extract_markdown_images(text)

        for image in images:

            str = f"![{image[0]}]({image[1]})"
            chunks = []
            if len(result) == 0:
                chunks = text.split(str)
            else:
                chunks = result.pop().text.split(str)
            for i, chunk in enumerate(chunks):
                if i == 1:
                    result.append(TextNode(image[0], 'image', image[1]))
                if len(chunk) > 0:
                    result.append(TextNode(chunk, default_type))

        final.append(result)

    return final

def split_nodes_link(old_nodes: str) -> List[TextNode]:
    final = []

    for node in old_nodes:

        result = []
        text = node.text
        default_type = node.text_type
        links = extract_markdown_links(text)

        for link in links:

            str = f"[{link[0]}]({link[1]})"
            chunks = []
            if len(result) == 0:
                chunks = text.split(str)
            else:
                chunks = result.pop().text.split(str)
            for i, chunk in enumerate(chunks):
                if i == 1:
                    result.append(TextNode(link[0], 'link', link[1]))
                if len(chunk) > 0:
                    result.append(TextNode(chunk, default_type))

        final.append(result)

    return final

node = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    'p',
)
new_nodes = split_nodes_image([node])
for n in new_nodes:
    for x in n:
        print(x)

"""
[
    TextNode("This is text with an ", text_type_text),
    TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
    TextNode(" and another ", text_type_text),
    TextNode(
        "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
    ),
]
"""
