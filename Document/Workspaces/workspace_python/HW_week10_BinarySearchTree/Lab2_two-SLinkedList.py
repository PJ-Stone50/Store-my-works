# Lab2 Na krub เมื่อไหร่จะเรียนรู้เรื่องนะวิชานี้

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
        while cur is not None:
            print("% 3d % -15s %-10s %2d" %(cur.id, cur.name, cur.lastname, cur.score))
            cur = cur.nextNode

    def addNewNode(self, newNode):
        if newNode is None:
            print("Error! Check your node")
            return False # fail to add a new node to a linked list as me.

        if self.headNode is NOnde:
            self.headNode = newNode
            return True
        cur = self.headNode

        if cur.id > newNode.id:
