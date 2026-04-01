class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        d = defaultdict(int)
        for num in nums:
            if d[num]:
                return True
            else:
                d[num] += 1
                
        return False
        