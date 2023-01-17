# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque 

graph = {
    1: [2,3,None],
    2: [4,None],
    3: [None],
    4: [5,6,None], 
    5: [6,None],
    6: [None]
}

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
llist.count()
print(llist.count())
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        