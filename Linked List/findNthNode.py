class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def getNthNode(self,index):
        current = self.head
        count = 0
        while current :
            if count == index:
                return current.data
            count += 1
            current = current.next
        assert(False)
        return 0

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
 
n = 3
print ("Element at index 3 is :", llist.getNthNode(n))        