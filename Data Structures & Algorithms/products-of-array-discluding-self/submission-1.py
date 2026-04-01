class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = [0]*len(nums)
        suf = [0]*len(nums)
        preprod = 1
        sufprod = 1

        i = 0
        while i < len(nums):
            pre[i]=preprod
            preprod *= nums[i]
            i += 1

        j = len(nums)-1
        while j >= 0:
            suf[j] = sufprod
            sufprod *= nums[j]
            j -= 1
        
        for k in range(len(nums)):
            nums[k] = pre[k]*suf[k]
        
        return nums

        