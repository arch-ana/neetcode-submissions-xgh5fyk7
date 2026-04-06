class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]

        for num, occ in freq.items():
            buckets[occ].append(num)

        res = []

        for i in range(len(buckets)-1, 0, -1):
            for items in buckets[i]:
                res.append(items)
                if len(res) == k:
                    return res

        return res
        


        