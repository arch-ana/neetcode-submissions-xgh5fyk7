class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        zeroes = 0

        for num in nums:
            if num == 0:
                zeroes += 1
                if zeroes > 1:
                    return [0]*len(nums)
            else:
                prod *= num


        for i in range(len(nums)):
            if zeroes == 1:
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = prod
            else:
                nums[i] = prod//nums[i]
        
        return nums

        