import xml.etree.ElementTree as ET


def load(path):
    tree = ET.parse(path)
    root = tree.getroot()
    return {root.tag: root.text}


def dump(data, path):
    # naive impl
    root_key = list(data.keys())[0]
    root = ET.Element(root_key)
    root.text = str(data[root_key])
    tree = ET.ElementTree(root)
    tree.write(path)

# TODO: nested support
# commented code below
# def advanced(): pass
