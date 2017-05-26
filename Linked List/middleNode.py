class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def getMiddleNode(self):
        slowptr = self.head
        fastptr = self.head
        if self.head != None:
            while fastptr != None and fastptr.next != None:
                fastptr = fastptr.next
                fastptr = fastptr.next
                slowptr = slowptr.next
            print("the middle element is", slowptr.data)


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)     
llist.push(6)
llist.push(7)
llist.getMiddleNode()       

