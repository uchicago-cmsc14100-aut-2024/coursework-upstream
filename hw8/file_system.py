import json

class Directory:
    """
    Class to represent a directory in a file directory system.

    Attributes:
        name (str): name of the directory
        contents (List[Directory or File]): a list of directories and files
            stored in the directory

    Methods:
        set_attribute (Dict[str, Any]): a method to set the attributes of
            the directory. Note: "contents" attribute is set in load_file_system
    """
    def __init__(self):
        self.name = None
        self.contents = []

    def set_attribute(self, data):
        self.name = data["name"]

    def __eq__(self, other):
        return ((self.name == other.name) and
                (self.contents == other.contents))
        
class File:
    """
    Class to represent a file in a file directory system.

    Attributes:
        name (str): name of the file
        text (str): the text stored in the file

    Methods:
        set_attributes (Dict[str, Any]): a method to set the attributes of
            the file
    """    
    def __init__(self):
        self.name = None
        self.text = None

    def set_attributes(self, data):
        self.name = data["name"]
        self.text = data["text"]

    def __eq__(self, other):
        return ((self.name == other.name) and
                (self.text == other.text))

def load_file_system(filename):
    """
    Load the file system from a file into a tree of Directory and File.

    Args:
        filename (str): name of a JSON file that stores a file system

    Return (Directory): the directory at the top of the file system
    """
    with open(filename) as j:
        data = json.loads(j.read())

    top = Directory()
    top.set_attribute(data)

    add_contents(top, data)

    return top

def add_contents(top, data):
    """
    Given the contents of a JSON file that stores a file system, create a
    tree of Directory and File objects that represent that file system.

    Args:
        top (Directory): The directory at the top of the file system
        data (Dict[str, Any]): Data from a JSON file that stores a file system. 

    Returns (None): Nothing, modifies top of the file system in-place
    """
    for item in data["contents"]:
        # create a new Directory
        if item["type"] == "Directory":
            d = Directory()
            d.set_attribute(item)
            add_contents(d, item)
            top.contents.append(d)

        # create a new File
        if item["type"] == "File":
            f = File()
            f.set_attributes(item)
            top.contents.append(f)

def file_systems_equal(system1, system2):
    """
    Compare two file systems for exact equality. Note: the two file systems must
        be exactly the same, including the order of any File or Directory 
        objects stored in the "contents" attribute of a Directory object. 

    Args:
        system1 (Directory or File): a file directory system
        system2 (Directory or File): another file directory system 

    Returns (bool): True if the file systems are equal, False otherwise. 
    """

    if not system1 == system2:
        return False

    if isinstance(system1, File):
        if not isinstance(system1, File):
            return False
        return system1 == system2

    if len(system1.contents) != len(system2.contents):
        return False

    for i in range(len(system1.contents)):
        if not file_systems_equal(system1.contents[i], system2.contents[i]):
            return False

    return True
