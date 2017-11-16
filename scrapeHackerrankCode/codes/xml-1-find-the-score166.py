# Accepted
# Python 3

def child_attrib(li):
    mylist = []; length = 0
    for i in range(len(li)):
        length += len(li[i].attrib)
        child = li[i].getchildren()
        if child:
            mylist.extend(li[i].getchildren())
    return length, mylist

def get_attr_number(root):

    li = root.getchildren()
    length = len(root.attrib)
    while li:
        leng, li = child_attrib(li)
        length += leng
    return length        

