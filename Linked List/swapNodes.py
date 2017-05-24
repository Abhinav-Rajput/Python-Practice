class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def swapNodes(self,x,y):
        if x == y:
            return
        prevX = None
        currX = self.head
        while (currX != None and currX.data !=x):
            prevX = currX
            currX = currX.next
        
        prevY = None
        currY = self.head
        while (currY != None and currY.data!= y):
            prevY = currY
            currY = currY.next
        
        if (currX == None) or (currY == None):
            return
        
        if prevX != None:
            prevX.next = currX
        else:
            self.head = currX
        
        if prevY != None:
            prevY.next = currY
        else:
            self.head = currY

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def printList(self):
        tNode = self.head
        while tNode != None:
            print(tNode.data,end=' ')
            tNode = tNode.next

# Driver program to test above function
llist = LinkedList()
 
# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print ("Linked list before calling swapNodes(4,3) ")
llist.printList()
llist.swapNodes(4, 3)
print ("\nLinked list after calling swapNodes(4,3) ")
llist.printList()            

        
