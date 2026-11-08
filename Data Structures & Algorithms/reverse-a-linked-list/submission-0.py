# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # A -> B -> null

        '''
        previous_node = A -> B -> None
        current_node = B -> None
        current_node.next = None
        next_node = None 

        A -> None
        '''
        # A -> B -> null
        previous_node = None # None 
        current_node = head # A

        while current_node is not None:
            next_node = current_node.next
            
            # A -> None
            current_node.next = previous_node

            # Move references
            previous_node = current_node # 
            current_node = next_node # 

        return previous_node

        