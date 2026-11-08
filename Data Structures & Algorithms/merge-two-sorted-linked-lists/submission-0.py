# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
            head = 
            l1_curr =
            l2_curr

            - looking at the end of current_node of each list
                - compare the values and determine the minimum
                - connect the head.next to the minimum node
        '''
        # [] [] 
        # list1 = [], list2 = [1,2] 
        # list1 = [3,4], list2=[]  

    

        dummy_head = ListNode() # dh->1->2->3->[4]->5
        curr_node = dummy_head # 5
        l1_curr = list1 # 6
        l2_curr = list2 # None

        # l1_curr is not None or l2_curr is not None
        while l1_curr and l2_curr: 
            if l1_curr.val <= l2_curr.val:
                curr_node.next = l1_curr # 3.next -> 4->6
                l1_curr = l1_curr.next # 6
            else:
                curr_node.next = l2_curr # 4.next -> 5
                l2_curr = l2_curr.next # None
            curr_node = curr_node.next # 5
                
        if l2_curr and l1_curr is None:
            curr_node.next = l2_curr
        elif l1_curr and l2_curr is None:
            curr_node.next = l1_curr #5->6

        return dummy_head.next 