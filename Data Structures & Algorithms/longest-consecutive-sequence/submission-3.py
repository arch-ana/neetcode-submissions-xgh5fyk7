class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums = set(nums)
        globalMax = 1

        for num in nums:
            currMax = 1
            if num-1 not in nums:
                
                consecutive = True
                nextNum = num+1
                while consecutive:
                    if nextNum in nums:
                        nextNum += 1
                        currMax += 1
                    else:
                        consecutive = False
            
            if currMax > globalMax:
                globalMax = currMax

        return globalMax
                        
        