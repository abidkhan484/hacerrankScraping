# Accepted
# Python 3

def get_attr_number(root):
    # here root is iterable; check the for loop
    return len(root.attrib)+sum(get_attr_number(node) for node in root)

