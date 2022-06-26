class Node:
    def __init__ (self, id=None):
        self.id = id
        self.nextNode = None

class SLinkedList:
    def __init__ (self):
        self.headNode = None

    def printList(self):
        cur = self.headNode
        if cur is not None:
            print(cur.id)
            cur = cur.nextNode

    def printRecursiveList(self, cur):
        if cur is not None:
            print(cur.id)
            self.printRecursiveList(cur.nextNode)

value = 10
list = SLinkedList()
list.headNode = Node(value)


while(cur is not None):
    newNode = Node(value)
    cur.nextNode = newNode
    cur = cur.nextNode




cur = list.headNode

list.printRecursiveList(cur)
list.printList()


