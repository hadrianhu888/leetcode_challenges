import linked_list
from linked_list import Node
from linked_list import LinkedList
llist = LinkedList()
print(llist)

first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

for node in llist:
    print(node)
