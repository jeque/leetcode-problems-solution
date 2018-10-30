class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """    
        pre = m-1
        for i in range(n-1,-1,-1):
            while pre>=0 and nums2[i]<nums1[pre]:
                nums1[pre+i+1] = nums1[pre]
                pre -= 1
            nums1[pre+i+1] = nums2[i]