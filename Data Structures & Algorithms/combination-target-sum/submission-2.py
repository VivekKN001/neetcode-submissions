class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def combSum(ind, nums, final_array, result, target):
            if target == 0:
                result.append(final_array.copy())
                return
            if ind >= len(nums) or target < 0:
                return
            
            final_array.append(nums[ind])
            combSum(ind, nums, final_array, result, target-nums[ind])

            final_array.pop()
            combSum(ind+1, nums, final_array, result, target)
            
        final_array, result = [], []
        combSum(0, nums, final_array, result, target)
        return result