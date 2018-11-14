class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if(J=='' or S==''):
            return 0
        jewel = collections.Counter(S)
        count = 0
        stone = [se for se in J]
        for jl in jewel:
            if jl in stone:
                count+=jewel[jl]
        return count