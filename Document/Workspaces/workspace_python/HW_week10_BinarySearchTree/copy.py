class Node:
    def __init__(self,dataVal = None):
        self.dataVal = dataVal 
        self.root = None
        self.right = None
        self.left = None

def Tree(data):
    if node.root is None:
        node.root = Node(data)
        return
        
    cur = node.root
    pre_node = None

    while cur:
        pre_node = cur
            
        if data < cur.dataVal:
            cur = cur.left
        else:
            cur = cur.right

    if data < pre_node.dataVal:
        pre_node.left = Node(data)
    else:
        pre_node.right = Node(data)

    

def data_tree():
    data = [3,1,2,4,5,6,0,9,11]
    for x in data:
        Tree(x) 
    
def printTreeInOrder(cur):
    if cur.left :
        printTreeInOrder(cur.left)
    print(cur.dataVal,end=", ")
    if cur.right:
        printTreeInOrder(cur.right)

node = Node()
data_tree()
printTreeInOrder(node.root)

