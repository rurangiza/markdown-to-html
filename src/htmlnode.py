
class HTMLNode:
    def __init__(self,
                 tag=None : str,
                 value=None : str,
                 children=None : list,
                 props=None : dict
    ):
        pass

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        res = ""
        for key, value in self.props.items():
            res += f' {key}="{value}"'
        return res
    
    def __repr__(self):
        return f'{}'
