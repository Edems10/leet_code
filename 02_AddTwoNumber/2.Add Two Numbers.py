# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1_list = []
        v2_list = []
        while l1 or l2 :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            v1_list.append(v1)
            v2_list.append(v2)
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        final_var = 0
        list_length = len(v2_list)
        for enumerator, (val_rev1, val_rev2) in enumerate(zip(v1_list[::-1], v2_list[::-1])):
            final_var += (10 ** ((list_length-1) - enumerator)) * val_rev1
            final_var += (10 ** ((list_length-1) - enumerator)) * val_rev2

        str_final_var = str(final_var)
        str_final_var = str_final_var[::-1]
        dummy = ListNode()
        current = dummy
        for str_l in str_final_var:
            print(str_l)
            current.next = ListNode(int(str_l))
            current = current.next
        
        return dummy.next

