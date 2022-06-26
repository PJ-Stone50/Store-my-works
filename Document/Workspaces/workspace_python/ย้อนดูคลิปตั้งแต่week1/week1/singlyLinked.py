class Node:
    def __init__(self, Id=None, name=None, value=None):
        self.Id = Id
        self.name = name
        self.value = value
        self.nextNode = None


class SLinkedList:
    def __init__(self):
        self.headNode = None

    def listprint(self):
        printval = self.headNode1
        
        while printval is not None:
            print(printval.Id)
            print(printval.name)
            print(printval.value)
            printval = printval.nextNode



def myOpenfile():
    f = open("data1.dat","r")
    if f.mode == "r":
        contents = f.read()
    f.close()

f = open("data1.dat","r")
content = f.read().splitlines()
content.sort()

#print(content, end = " ")

list = SLinkedList()
list.headNode = Node(content)
cur = list.headNode


list2 = SLinkedList()
list2.headNode = Node(content)




for line in f:
    newNode = Node(line)
    cur.nextNode = newNode
    cur = cur.nextNode

#list.listprint()
print(cur.Id)
