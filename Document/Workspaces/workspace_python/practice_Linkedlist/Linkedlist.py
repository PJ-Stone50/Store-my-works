class Node:
    def __init__(self, dataval=None, nextNode=None):
        self.dataval = dataval
        self.nextNode = nextNode


class Linkedlist:
    def __init__(self):
        self.headNode = None

    def insert_at_begining(self, dataval):
        node = Node(dataval, self.headNode)
        self.headNode = node

    
    def printlist(self):
        if self.headNode is None:
            print("Linked list is empty")
            return

        cur = self.headNode
        output = ''
        while(cur):
            output += str(cur.dataval) + '-->'
            cur = cur.nextNode

        print(output)

    def insert_at_end(self, dataval):
        if self.headNode is None:
            self.headNode = Node(dataval, None)
            return



        cur = self.headNode
        while (cur.nextNode):
            cur = cur.nextNode

        cur.nextNode = Node(dataval, None)

    def insert_values(self, data_list):
        self.headNode = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        cur = self.headNode
        while(cur):
            count += 1
            cur = cur.nextNode

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.headNode = self.headNode.nextNode
            return

        count = 0
        cur = self.headNode
        while(cur):
            if count == index -1:
                cur.nextNode = cur.nextNode.nextNode # At this situation, I งงหนัก งงแบบตึบๆ มึนๆ เอ๋อเบาๆ บางทีก็หลุดไปเลย
                break
            cur = cur.nextNode
            count += 1


list = Linkedlist()
# list.insert_at_end(51)
# list.insert_at_begining(9)
# list.insert_at_end(3)
list.insert_values(["A","O","N","G","A<--"])

list.printlist()

print("Length: ",list.get_length())
list.remove_at(4)
list.printlist()
print("Length: ",list.get_length())