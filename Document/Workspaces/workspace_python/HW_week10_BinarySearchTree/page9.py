class Node:
    def __init__ (self, dataval=None):
        self.dataval = dataval
        self.nextNode = None

class SLinkedList:
    def __init__ (self):
        self.headNode = None

    def listPrint(self):
        printval = self.headNode
        while (printval):
            print(printval.dataval, end="\n")
            printval = printval.nextNode

    def AtEnd(self, newdata):
        newNode = Node(newdata)
        
        if self.headNode is None:
            print("***First Node has been created***")
            self.headNode = newNode
            return

        last = self.headNode
        
        while(last.nextNode):
            last = last.nextNode
        last.nextNode = newNode


    

list = SLinkedList()
list.headNode = Node("Mon")
cur = list.headNode

e2 = Node("Tue")
e3 = Node("Wed")



list.headNode.nextNode = e2

e2.nextNode = e3

list.AtEnd("atEnd")
list.AtEnd("3")


while(cur):
    print(cur.dataval)
    cur = cur.nextNode

# list.listPrint()
