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

    def detectLoop(self):
        slowp = self.head
        fastp = self.head
        while slowp and fastp and fastp.next:
            slowp = slowp.next
            fastp = fastp.next.next
            if slowp == fastp:
                print('found loop')
                return

# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
 
# Create a loop for testing
llist.head.next.next.next.next = llist.head
llist.detectLoop()