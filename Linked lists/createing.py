

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Singly_linked_list:
    def __init__(self) :
        self.head = None
    
    def insert_beginig(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    def insert_end(self,data):
        ne  = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne
    
    def insert_at_position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.next = temp.next
        temp.next = np
        print("\n",temp.data)

    def desplay_list(self):
        if self.head is None:
            print("List is Empty..!")
        else:
            temp = self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next

l = Singly_linked_list()
l.insert_beginig(2)
l.insert_beginig(8)
l.insert_end(1)
l.insert_at_position(1,6)
l.desplay_list()
