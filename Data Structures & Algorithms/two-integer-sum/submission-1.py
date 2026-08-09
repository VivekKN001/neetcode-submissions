class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums:
                j = nums.index(complement)
                if i != j:
                    if i > j:
                        return [j, i]
                    return [i, j]

        return []