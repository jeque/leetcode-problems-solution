class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse(prev, cur):                
            if cur:
                reverse(cur, cur.next)
                cur.next = prev
            else:
                nonlocal head
                head = prev
        reverse(None, head)
        return head