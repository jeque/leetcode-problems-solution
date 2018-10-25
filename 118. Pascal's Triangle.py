class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        Pascal = []
        if numRows == 0:
            return Pascal
        Pascal_Tmp = []
        for i in range(numRows):
            Pascal_Tmp = [1] + Pascal_Tmp 
            for j in range(1,len(Pascal_Tmp)-1):
                Pascal_Tmp[j] += Pascal_Tmp[j+1]
            Pascal.append(Pascal_Tmp)
        return Pascal