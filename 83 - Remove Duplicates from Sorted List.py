#Given a sorted linked list,
#delete all duplicates such that each element appear only once.

#Example 1:

#Input: 1->1->2
#Output: 1->2


#Example 2:

#Input: 1->1->2->3->3
#Output: 1->2->3


#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def deleteDuplicates(head: ListNode) -> ListNode:
    # make a list to check if there is allready a node val in it
    node_val=[]
    pre_point=cur_point=head

    while cur_point:
        if cur_point.val in node_val:
            cur_point=cur_point.next
            pre_point.next=cur_point
        else:
            node_val.append(cur_point.val)
            if pre_point!=cur_point:
                pre_point=pre_point.next
            cur_point=cur_point.next
#Input: 1->1->2
#Output: 1->2

    return head

def print_nodes(point):
    while point.next:
        print( point.val,"->",end='')
        point=point.next
    print(point.val)

# test
#Input: 1->1->2
#Output: 1->2
head=ListNode(1)
head.next=ListNode(1)
head.next.next=ListNode(2)
print_nodes(head)
after=deleteDuplicates(head)
print_nodes(after)

#Input: 1->1->2->3->3
#Output: 1->2->3
print("==============")
head=ListNode(1)
head.next=ListNode(1)
head.next.next=ListNode(2)
head.next.next.next=ListNode(3)
head.next.next.next.next=ListNode(3)
print_nodes(head)
after=deleteDuplicates(head)
print_nodes(after)
