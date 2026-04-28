class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d = defaultdict(int)

        for i in range(len(numbers)):
            if target - numbers[i] in d:
                return [d[target-numbers[i]], i+1]
            else:
                d[numbers[i]] = i+1

        return []
        
        