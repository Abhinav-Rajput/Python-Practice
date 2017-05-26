class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def reverseList(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print ("Given Linked List")
llist.printList()
llist.reverseList()
print ("\nReversed Linked List")
llist.printList()            

