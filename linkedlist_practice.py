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
llist.appendleft('z')
print(llist)
llist.popleft()
print(llist)

queue = deque()
print(queue)

queue.append('Mary')
queue.append('John')
queue.append('Susan')
print(queue)
print(deque(queue))
queue.popleft()
print(queue)
queue.popleft()
print(queue)

history = deque()
history.appendleft("https://github.com/")
history.appendleft("https://realpythons.org/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
print(deque(history))

history.popleft()
print(history)
history.popleft()
print(history)

