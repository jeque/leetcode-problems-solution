class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            length = 0
        length= len(list(set(nums)))
        elem = sorted(list(set(nums)))
        if length:
            for i in range(length):
                nums[i] = elem[i]
        return length