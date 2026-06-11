import xml.etree.ElementTree as ET


def load(path):
  tree = ET.parse(path)
  root = tree.getroot()
  return {root.tag: root.text}

def dump(data, path):
  # naive impl
  rootKey = list(data.keys())[0]
  root = ET.Element(rootKey)
  root.text = str(data[rootKey])
  Tree = ET.ElementTree(root)
  Tree.write(path)

# TODO: nested support
# commented code below
# def advanced(): pass
