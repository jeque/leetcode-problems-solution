class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int pre = nums[0];
        vector<int> result(nums.size(), 1);
        for(int i = nums.size()-2; i >= 0; i--) {
            result[i] = nums[i+1] * result[i+1];
        }
        for(int i = 1; i < nums.size(); i++) {
            result[i] = pre * result[i];
            pre *= nums[i];
        }
        return result;    
    }
};