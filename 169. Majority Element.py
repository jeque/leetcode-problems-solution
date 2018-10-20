class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for Element in nums:
            if count == 0:
                MajorElem = Element 
            count += (1 if Element == MajorElem else -1)
        return MajorElem