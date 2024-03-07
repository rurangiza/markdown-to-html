
from typing import List, Dict
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        self.value = value # string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children # list of HTMLNode objects representing the children of this node
        self.props = props # dictionary of key-value pairs representing the attributes of the HTML tag

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props == None:
            return
        res = ""
        for key, value in self.props.items():
            res += f' {key}="{value}"'
        return res
    
    def __repr__(self):
        return f' tag:{self.tag}\n value:{self.value}\n children:{self.children}\n props:{self.props}'
