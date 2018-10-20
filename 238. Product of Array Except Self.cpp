/*
思路：设nums=[2,3,4,5],
将数组的每个元素分为左边的乘积和右边的乘积，之后将左右乘积再相乘得到结果。若为右边第一个元素，无右乘积，则右乘积等于1，左边第一个元素同理。
1.第一个for循环：首先创建一个长度跟输入数组nums一样的数组result，并把所有元素置1，之后对result数组从右向左开始循环，所得的数组为result[i]（即元素右乘积）结果result为[3*4*5,4*5,5,1]；
2.之后再使用一个for循环，从第一个元素开始循环，result[i] = pre * result[i];，所得的result即为所求的值，这里pre每次需要乘上nums[i]保持更新，pre为[1,2,2*3,2*3*4]。
*/
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int pre = nums[0];
        vector<int> result(nums.size(), 1); #初始化输出
		# 元素右乘积
        for(int i = nums.size()-2; i >= 0; i--) {
            result[i] = nums[i+1] * result[i+1];
        }
		# 元素左遍历
        for(int i = 1; i < nums.size(); i++) {
            result[i] = pre * result[i];
            pre *= nums[i];
        }
        return result;    
    }
};