class Node:
    def __init__ (self, dataval=None):
        self.dataval = dataval
        self.nextNode = None

class SLinkedList:
    def __init__ (self):
        self.headNode = None

    def AddNodewithKey(self, key, newNode):
        if self.headNode is None:
           print("Empty linked list")
           return
        cur = self.headNode

        while (cur.nextNode):
            if (cur.dataval == key):
                break;

            cur = cur.nextNode

        if cur is not None:
            newNode.nextNode = cur.nextNode
            cur.nextNode = newNode

    def printLinkedList(self):
        cur = self.headNode
        while cur is not None:
            print(cur.dataval)
            cur = cur.nextNode

list = SLinkedList()
list.headNode = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list.headNode.nextNode = e2 # headNode ถัดจาก Mon

e2.nextNode = e3

newNode = Node("Wed")
newNode2 = Node("Node2")
list.AddNodewithKey("Wed", newNode)
list.AddNodewithKey("Node2", newNode2)


cur = list.headNode
while (cur):
    print(cur.dataval)
    cur = cur.nextNode



print("Result ")

# list.printLinkedList()