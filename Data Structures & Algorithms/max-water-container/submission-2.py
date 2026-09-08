class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPointer, rightPointer = 0, len(heights)-1
        result = 0
        while leftPointer < rightPointer:
            area = (rightPointer - leftPointer) * min(heights[leftPointer], heights[rightPointer])
            result = max(result, area)
            if heights[leftPointer] <= heights[rightPointer]:
                leftPointer+=1
            else:
                rightPointer-=1
        
        return result