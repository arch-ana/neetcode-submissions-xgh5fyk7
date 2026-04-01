class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}

        for x in range(len(nums)):
            if nums[x] in dict:
                return [dict[nums[x]],x]
            else:
                dict[target-nums[x]] = x
        