from typing import List, Dict

class HTMLNode:
    def __init__(self,
                 tag: str=None,
                 value: str=None,
                 children: List['HTMLNode']=None,
                 props: Dict[str, str]=None
        ) -> None:
        # the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.tag = tag
        # the value of the HTML tag (e.g. the text inside a paragraph)
        self.value = value
        # list of HTMLNode objects representing the children of this node
        self.children = children
        # dictionary of key-value pairs representing the attributes of the HTML tag
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if self.props == None:
            return
        res = ""
        for key, value in self.props.items():
            res += f' {key}="{value}"'
        return res
    
    def __eq__(self, other):
        return self.tag == other.tag \
            and self.value == other.value \
            and self.children == other.children \
            and self.props == other.props
    
    def __repr__(self) -> str:
        return f'\n tag:{self.tag}\n value:{self.value}\n children:{self.children}\n props:{self.props}\n'

class LeafNode(HTMLNode):
    def __init__(self,
                tag: str,
                value: str,
                props: Dict[str, str]=None
        ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leafnode's value not set")

        if not self.tag:
            return self.value

        res = "<" + self.tag
        if self.props:
            res += self.props_to_html()
        res += ">"
        res += self.value
        res += '</' + self.tag + '>'
        return res

class ParentNode(HTMLNode):
    def __init__(self,
                tag: str,
                children: List[HTMLNode],
                props: Dict[str, str]=None
        ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('tag was not provided')
        if not self.children or len(self.children) == 0:
            raise ValueError('no children in parent node')
    
        res = f'<{self.tag}>'
        for child in self.children:
            res += child.to_html()
        res += f'</{self.tag}>'
        return res