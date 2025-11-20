class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Llist:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def delete(self, value):
        curr = self.head
        prev = None

        if curr and curr.value == value:
            self.head = curr.next
            return True
        
        while curr:
            if curr.value == value:
                prev.next = curr.next
                return 
            
    

    def print(self):
        t = self.head
        while t != None:
            print(t.value,end=" -> ")
            t = t.next
        print(None)

l1 = Llist()
l1.prepend(10)
l1.prepend(20)
l1.prepend(30)
l1.append(40)
l1.append(50)
l1.delete(20)
l1.print()