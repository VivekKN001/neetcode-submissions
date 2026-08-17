class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0: # This means did we already visted that location
                return abs(num)
            
            nums[idx] *=-1 # if not visted previously, we do negative marking of that location
        return -1