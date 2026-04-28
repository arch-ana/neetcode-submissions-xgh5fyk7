class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d = defaultdict(int)
        result = []

        for i in range(len(numbers)):
            if target - numbers[i] in d:
                result.append(d[target-numbers[i]])
                result.append(i+1)
            else:
                d[numbers[i]] = i+1

        return result
        
        