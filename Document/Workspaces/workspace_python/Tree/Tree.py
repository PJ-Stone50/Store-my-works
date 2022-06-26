class Node:
    def __init__ (self, dataval=None):
        self.dataval = dataval
        self.right = None
        self.left = None
        self.nextNode = None

class SLinkedList:
    def __init__ (self):
        self.headNode = None

    def addNewNode(self,key, newNode):
        if newNode is None:
            print("Empty Node")
            return False
        
        if self.headNode is None:
            self.headNode = newNode
            return True
        cur = self.headNode

        while (cur.nextNode):
            if (cur.dataval == key):
                break;

            cur = cur.nextNode

        if cur is not None:
            newNode.nextNode = cur.nextNode
            cur.nextNode = newNode

    def listPrint(self):
        cur = self.headNode
        while(cur):
            print(cur.dataval)
            cur = cur.nextNode
        
       #0,1,2,3,4,5,6,7,8
data = [3,1,2,4,5,6,0,9,11]


root = None
root = Node(data[7]) #9
cur = root
newNode = Node(data[4])
cur.left = newNode # ชี้ 5

newNode = Node(data[5])
cur = cur.left
cur.right = newNode # ชี้ 6

cur = root
newNode = Node(data[8])
cur.right = newNode

cur = cur.left
newNode = Node(data[0])
cur.left = newNode


print(root.dataval)
cur = root.left
print(cur.dataval)
cur = cur.right
print(cur.dataval)
cur = root.right
print(cur.dataval)
cur = cur.left
print(cur.left.dataval)

