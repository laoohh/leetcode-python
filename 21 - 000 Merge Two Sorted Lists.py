#!!!!!!!!!!!!!!!!
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of
# the first two lists.
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

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(0)
    new_list = head

    while True:
        if l1 is None:
            new_list.next = l2
            break
        elif l2 is None:
            new_list.next = l1
            break
        if l1.val <= l2.val:
            new_list.next = l1
            new_list = new_list.next
            l1 = l1.next
        elif l1.val > l2.val:
            new_list.next = l2
            new_list = new_list.next
            l2 = l2.next

    return head.next

#2222222222222222222222222222222
def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
    head = new_list = ListNode(0)
    node1 = l1; node2 = l2
    while(node1 or node2):
        if None == node1:
            new_list.next = node2
            break
        elif None == node2:
            new_list.next = node1
            break
        elif node1.val > node2.val:
            new_list.next = new_list = ListNode(node2.val)
            node2 = node2.next
        else:
            new_list.next = new_list = ListNode(node1.val)
            node1 = node1.next
    return head.next
