class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {

        int length = nums.size()*2;
        vector<int> arr;
        
        for (int i = 0; i < length; i++){
            if (i < nums.size()){
                arr.push_back(nums[i]);
            }
            else{
                arr.push_back(nums[i - nums.size()]);
            }
        }

        return arr;
    }

};