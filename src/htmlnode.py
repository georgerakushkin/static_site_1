class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        else:
            pairs = self.props.items()
            list_of_pairs = []
            for key, value in pairs:
                propstr = (f" {key}='{value}'")
                list_of_pairs.append(propstr)
            joined_list = "".join(list_of_pairs)
            return joined_list;

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return str(self.value)
        else:
            p = self.props_to_html()
            return f"<{self.tag}{p}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError ("cant be none")
        if len(self.children) == 0:
            raise ValueError ("no children found")
        
        children_stringed = []
        for child in self.children:
            p = child.to_html()
            children_stringed.append(p)
        joined_list = "".join(children_stringed)
        
        #props_stringed = []
        #for prop in self.props:
        #    p = prop.props_to_html()
        #   props_stringed.append(p)
        #joined_props = "".join(props_stringed)

        return f"<{self.tag}{self.props_to_html()}>{joined_list}</{self.tag}>"    


    

        

