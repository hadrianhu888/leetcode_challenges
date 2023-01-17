from collections import deque 

graph = {
    1: [2,3,None],
    2: [4,None],
    3: [None],
    4: [5,6,None], 
    5: [6,None],
    6: [None]
}
print(graph.values)
deque(['a', 'b', 'c', 'd', 'e', 'f'])
deque()
deque(['a', 'b', 'c', 'd'])
print(deque(['a', 'b', 'c']))
print(deque(['abc']))
print(deque([{'data': 'a'},{'data': 'b'},{'data': 'c'}]))
llist = deque(['abcdef'])
print(llist)
llist.append("g")
print(llist)
llist.pop()
print(llist)
llist.count(deque)
print(llist.count(deque))

