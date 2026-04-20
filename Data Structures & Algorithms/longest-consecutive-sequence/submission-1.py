class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
            
        nums = set(nums)

        globalMax = 1

        for num in nums:
            currMax = 1
            if num - 1 not in nums:
                consecute = True
                nextNum = num+1
                while consecute:                    
                    if nextNum in nums:
                        currMax += 1
                        nextNum += 1
                    else:
                        consecute = False
            
            if currMax > globalMax:
                globalMax = currMax

        return globalMax
        