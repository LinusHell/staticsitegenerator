from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str ,children: list[HTMLNode], props: dict[str,str] | None = None):
        super(ParentNode,self).__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag is missing for ParentNode")
        if self.children is None:
                    raise ValueError("Children are missing for ParentNode")
        children_html = ""
        for child in self.children:
              children_html += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
        