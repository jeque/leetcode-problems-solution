class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
    //选出最短的，然后从后往前扫描
    string res = "";
    if(strs.size()==0)
        return res;
    sort(strs.begin(),strs.end());
    int length1 = strs[0].length();
    
    for(int i = 0;i<length1;i++)
    {
        bool flag = true;
        for(int j =1;j<strs.size();j++)
        {
            if(strs[j][i] != strs[0][i])
                return res;
        }
        res.push_back(strs[0][i]);
    }
    return res;
    }
};