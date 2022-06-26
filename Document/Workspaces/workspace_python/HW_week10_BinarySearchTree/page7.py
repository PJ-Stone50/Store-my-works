class Node:
    def __init__ (self, dataval=None):
        self.dataval = dataval
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    def listprint(self):
        printval = self.headNode
        while printval is not None:
            print(printval.dataval, end="")
            printval = printval.nextNode

    
def myOpenfile():
    f = open("data1.dat","r")
    # f2 = open("data2.dat","readonly")
    if f.mode == "r":
        content = f.read()
        f.close()    
        # return
        
    
    


f = open("data1.dat","r")
content = f.readline()

# f2 = open("data2.dat","r")
# content2 = f2.readline()

# myOpenfile()
list = SLinkedList()
list.headNode = Node(content)
cur = list.headNode

# for content in f:
#     newNode = Node(content)
#     cur.nextNode = newNode
#     cur = cur.nextNode

while(cur):
    print(cur.dataval)
    cur = cur.nextNode

# list.listprint()



# f2.close()