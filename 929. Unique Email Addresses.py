class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = []
        for each in emails:
            res = re.match('(.*?)\++.*@(.*)',each)
            result.append(res.group(1).replace('.','')+'@'+res.group(2))
        result = set(result)
        return len(result)