class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxProd = 0
        l, r = 0, len(heights)-1

        while l<r:
            currProd = min(heights[l], heights[r])*(r-l)
            maxProd = max(maxProd, currProd)
            if min(heights[l], heights[r]) == heights[l]:
                l += 1
            else:
                r -= 1

        return maxProd
            

        