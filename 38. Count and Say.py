class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1: 
            return '1' 
        beforeInt='1'
        afterInt='' 
        while n>1: 
            curLen=len(beforeInt) 
            new=beforeInt[0]
            count=0 
            afterInt='' 
            for i in range(curLen): 
                if beforeInt[i]==new: 
                    count+=1 
                    if i==curLen-1: 
                        afterInt+=(str(count)+new) 
                else: 
                    afterInt+=(str(count)+new) 
                    new=beforeInt[i] 
                    count=1 
                    if i==curLen-1: 
                        afterInt+=(str(count)+new) 
            beforeInt=afterInt 
            n-=1 
        return afterInt
