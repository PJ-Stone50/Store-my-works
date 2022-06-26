class Node:
    def __init__ (self, id=None, name=None, lastname=None, score=None):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.score = score
        self.nextNode = None

class SLinkedList:
    def __init__(self):
        self.headNode = None

    def listPrint(self):
        cur = self.headNode
        while(cur):
            print("% 3d % -15s %-10s %2d"%(cur.id, cur.name, cur.lastname, cur.score))
            cur = cur.nextNode


    def addNewNode(self, newNode):
        if newNode is None:
            print("Empty Node, Check your newNode!")
            # print(int(id), name, lastname, int(score))
            return False

        if self.headNode is None: # ถ้าโหนดว่างเปล่าเฉกเช่นสมองข้า
            print("Linked List สายนี้ยังไม่มีโหนดเลย ข้าจะเสกใหม่ให้เจ้าละกัน..!")
            self.headNode = newNode # เซ็ตให้โหนดใหม่ที่รับค่าเข้ามาเป็น self.headNode
        
            return True # เอาไปเช็คอะไรสักอย่างได้ไำหม

        cur = self.headNode # cur ปัจจุบันอยู่ที่ head

        if cur.id > newNode.id: #
            newNode.nextNode = self.headNode # โหนดใหม่ เอาไปชี้ท้าย self.headNode
            self.headNode = newNode
            return True

        ## ตรงนี้น่าจะมีบอกใน week ก่อนๆ ค่อยกลับไปหาดู
        
        afterCur = self.headNode # มึนไปหมดล้า
        cur = afterCur.nextNode

        while(cur):
            if(cur.id > newNode.id):
                break
            afterCur = cur
            cur = cur.nextNode

        newNode.nextNode = cur
        afterCur.nextNode = newNode

# ทำไมเราไม่มาทำอันนี้ก่อนน้า เขกกะโหลกตัวเองแรงๆ บ้าบอคอหอยพอกจิงๆเลยเชียว สติมีส่วนสำคัญมากๆเลยแหละ
lines = open("name1.txt").readlines()

list1 = SLinkedList()
items = []

print("===============================")
print("Print From name1.txt")
for line in lines:

    id, name, lastname, score = line.split()

    print(id," ",name," ",lastname,score)

    newNode = Node(int(id), name, lastname, int(score))
    e = Node(99,"A","LastA",9)
    list1.addNewNode(newNode)

print("===============================")

# list1.listPrint()
## myHead is a boom boom


