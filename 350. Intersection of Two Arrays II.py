class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_result = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                num_result.append(nums1[i])
                nums2.remove(nums1[i]) 
        return num_result