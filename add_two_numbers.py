# Definition for singly-linked list.
""" class ListNode(object):
def __init__(self, val=0, next=None):
self.val = val
self.next = next """

import linked_list
from linked_list import *

""" class Node:
def _init__(self, data):
self.data = data
self.next = None """


class Solution(object):
    def addTwoNumbers(self, first, second):
        """
        :type first: ListNode
        :type second: ListNode
        :rtype: ListNode
        """
        first = LinkedList([])
        second = LinkedList([])
        prev = None
        temp = None
        carry = 0
        while first is not None and second is not None:
            if first is None:
                firstData = 0
            else:
                firstData = first.data
            if second is None:
                secondData = 0
            else:
                secondData = second.data
            sum = carry
            sum += firstData
            sum += secondData
            if sum > 10:
                carry = 1
            else:
                carry = 0
            sum %= 10
            temp = Node(sum)
            if self.head is None:
                self.head = temp
            else:
                self.next = temp
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)

    def subTwoNumbers(self, first, second):
        """
        subtracts two lists of numbers via linked list
        :type first: ListNode
        :type second: ListNode
        :return type: ListNode 
        """
        prev = None
        temp = None
        carry = 0
        while first is not None and second is not None:
            if first is None:
                firstData = 0
            else:
                firstData = first.data
            if second is None:
                secondData = 0
            else:
                secondData = second.data
            diff = carry
            diff -= firstData
            diff -= secondData
            if diff > 10:
                carry = 1
            else:
                carry = 0
            diff %= 10
            temp = Node(diff)
            if self.head is None:
                self.head = temp
            else:
                self.next = temp
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
def main():
    """Test out the functions"""
    first = Node(2)
    first.next = Node(4)
    first.next.next = Node(3)
    second = Node(5)
    second.next = Node(6)
    second.next.next = Node(4)
    s = Solution()
    s.addTwoNumbers(first, second)
    s.printList()
    s.subTwoNumbers(first, second)
    s.printList()

if __name__ == "__main__":
    main()
    
