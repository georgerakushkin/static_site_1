class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None): #props is a dictionary of properties
        self.tag = tag #tag is the name of the html tag
        self.value = value #value is the actual text content of the node
        self.children = children #children is a list of HTMLNodes
        self.props = props #props is a dictionary of properties
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self): #converts the props dict to a string in html format
        if self.props == None:
            return ""
        else:
            pairs = self.props.items()  #returns a list of tuples of key value pairs found in the props dictionary
            list_of_pairs = []  # creates a new list to store the properties as strings
            for key, value in pairs: #for every key value pair in our tuple list
                propstr = (f" {key}='{value}'")     #creates a string with the key and value of the property
                list_of_pairs.append(propstr) #and then appends it to our list of pairs
            stringed_list = "".join(list_of_pairs) #joins the list of pairs into a single string
            return stringed_list; #returns the joined list

class LeafNode(HTMLNode): #a leaf node is a node that has no children
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, props) #inherits from the HTMLNode class and passes the tag, value, and props to the HTMLNode constructor

    def to_html(self): #converts the leaf node to a string in html format
        if self.value == None: #if there is no text content, raise an error
            raise ValueError
        if self.tag == None: #if there is no tag, return the text content as a string
            return str(self.value)
        else:
            p = self.props_to_html() #converts the props dict to a string in html format
            return f"<{self.tag}{p}>{self.value}</{self.tag}>" #returns the tag, props, and text content as a string in html format
        
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children, props: dict = None):
        super().__init__(tag, children, props) #inherits from the HTMLNode class and passes the tag, children, and props to the HTMLNode constructor
    
    def to_html(self):
        if self.tag == None: #if there is no tag, raise an error
            raise ValueError ("cant be none")
        if len(self.children) == 0: #if there are no children, raise an error
            raise ValueError ("no children found")
        
        children_stringed = [] #create a new list that will store the children as strings 
        for child in self.children: #for every child in the children list
            p = child.to_html() #converts the child to a string in html format
            children_stringed.append(p) #and then appends it to our list of children
        joined_list = "".join(children_stringed) #joins the list of children into a single string

        return f"<{self.tag}{self.props_to_html()}>{joined_list}</{self.tag}>" #returns the tag, props, and children as a string in html format


    

        

