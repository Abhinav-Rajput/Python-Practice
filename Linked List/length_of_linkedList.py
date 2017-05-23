class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def getCount(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

llist = LinkedList()                
llist.push(1)
llist.push(3)
llist.push(1)
llist.push(2)
llist.push(1)

print("Count pf Node is",llist.getCount())
