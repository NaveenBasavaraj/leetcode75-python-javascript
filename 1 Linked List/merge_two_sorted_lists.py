# merge two sorted lists
from nodes import LinkedListNode

class Merge:
    '''
    1. take dummy node
    2. check if node1 and node2 exists
    3. compare node1.val and node2.val and to assign dummynode.next 
    4. return dummy node 
    '''
    def merge_two_sorted_list(self, list1, list2):
        dummy = node = LinkedListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next 
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2 
        
        return dummy.next