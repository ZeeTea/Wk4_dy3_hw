#Create a function that takes in a list and converts it to a linked list. 
# Create and use a decorator which sorts the function's input list. 
# For an extra point sort with one of the algorithms learned this week.
#Hint: You will need to some some additional research on accessing a function's parameter from a decorator.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

def sort_input_list(func):
    def wrapper(lst):
        sorted_lst = sorted(lst)
        return func(sorted_lst)
    return wrapper

@sort_input_list
def convert_to_linked_list(lst):
    linked_list = LinkedList()
    for item in lst:
        linked_list.add_node(item)
    return linked_list

lst = [3, 1, 4, 5, 9, 2, 6]

linked_list = convert_to_linked_list(lst)

current_node = linked_list.head
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next
