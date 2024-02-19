from nodes import LinkedListNode

# reverse a linked list

class Solution:
    '''
    starting from root, for each node we need three things
    1. take next node in temp reference
    2. point current node's next pointer to previous node
    3. now start working on next node (stored in temp reference) 
    '''
    def reverse_linked_list(self, head: LinkedListNode) -> LinkedListNode:
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev # this is the last node
            
