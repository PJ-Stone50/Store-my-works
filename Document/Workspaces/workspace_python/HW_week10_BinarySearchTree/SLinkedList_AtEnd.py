class Node:
    def __init__ (self, dataval=None):
        self.dataval = dataval
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    def AtEnd(self, newdata):

        NewNode = Node(newdata)

        if self.headNode is None:
            self.headNode = NewNode
            return
        lastest = self.headNode
        while(lastest.nextNode):
            lastest = lastest.nextNode
        lastest.nextNode = NewNode
        print(NewNode.dataval)

    def AddNodewithKey(self, key, newdata):
        newNode = Node(newdata)
        if self.headNode is None:
            print("Create First Node in SLinkedList")
            self.headNode = newNode
            return
        cur = self.headNode # Mon
        

        while cur.nextNode is not None: # ตราบใดที่ยังไม่ None
            if (cur.dataval == key): #งง key
                break;
            cur = cur.nextNode

        if cur is not None:
            newNode.nextNode = cur.nextNode
            cur.nextNode = newNode
     

    def listprint(self):
        cur = self.headNode
        while(cur):
            if cur.dataval%2 != 0:
                cur.dataval += 1
            print(cur.dataval, end=", ")
            cur = cur.nextNode



numbers = [1,4,5,6,9,15,22,32,2,6,7, 3, 11, 12, 66,78,31, 34]
list = SLinkedList()

list.headNode = Node(numbers[0])


e2 = Node(numbers[1])
e3 = Node(numbers[2])
e4 = Node(numbers[3])
e5 = Node(numbers[4])
e6 = Node(numbers[5])
e7 = Node(numbers[6])
e8 = Node(numbers[7])
e9 = Node(numbers[8])
e10 = Node(numbers[9])
e11 = Node(numbers[10])
e12 = Node(numbers[11])
e13 = Node(numbers[12])
e14 = Node(numbers[13])
e15 = Node(numbers[14])
e16 = Node(numbers[15])
e17 = Node(numbers[16])
e18 = Node(numbers[17])


list.headNode.nextNode = e2
e2.nextNode = e3
e3.nextNode = e4
e4.nextNode = e5
e5.nextNode = e6
e6.nextNode = e7
e7.nextNode = e8
e8.nextNode = e9
e9.nextNode = e10
e10.nextNode = e11
e11.nextNode = e12
e12.nextNode = e13
e13.nextNode = e14
e14.nextNode = e15
e15.nextNode = e16
e16.nextNode = e17
e17.nextNode = e18


# newNode = Node("Wed")

# list.AddNodewithKey(4, "Thu'")




cur = list.headNode

# while ( cur):
#     #print(cur.dataval)
#     cur = cur.nextNode
    
# cur = list.headNode
# while( cur.dataval != "Tue"):
#     cur = cur.nextNode


# curl = cur.nextNode
# cur.nextNode = curl.nextNode
# del curl




list.listprint()

