class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0 :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True 
    


my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(3)
my_ll.print_list()





# def append(self, value):
#     while self.head and self.next is not None:
#         self.next 
#     if self.next == None:
#         self.next  = value
#     elif self.head == None:
#         self.head = value
