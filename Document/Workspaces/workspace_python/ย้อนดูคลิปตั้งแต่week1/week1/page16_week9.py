class Node:
    def __init__(self, dataVal=None):
        self.datatVal = dataVal
        self.right = None
        self.left = None

data = [3,1,2,4]
root = None
root = Node(3)
cur = root
newNode = Node(1)
cur.left = newNode

newNode = Node(2)
cur = cur.left
cur.right = newNode

cur = root
newNode = Node(4)
cur.right = newNode

print(root.datatVal)
cur = root.left

print(cur.datatVal)
cur = cur.right

print(cur.datatVal)
cur = root.right

print(cur.dataVal)
