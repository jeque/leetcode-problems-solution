class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_ = []
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                list_ += [l1.val]
                l1 = l1.next
            else:
                list_ += [l2.val]
                l2 = l2.next
        
        while l1 != None:
            list_ += [l1.val]
            l1 = l1.next
        while l2 != None:
            list_ += [l2.val]
            l2 = l2.next         
        return list_ 