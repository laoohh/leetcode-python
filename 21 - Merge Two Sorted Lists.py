#!!!!!!!!!!!!!!!!
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example::  
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
