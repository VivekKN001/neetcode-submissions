class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def combinationSumII(ind, nums, n, result, final_array, target):
            if target == 0:
                result.append(final_array.copy())
                return 
            
            for i in range(ind,n):
                if i>ind and nums[i] == nums[i-1]:
                    continue

                if nums[i] > target:
                    break

                final_array.append(nums[i])
                combinationSumII(i+1, nums, n, result, final_array, target-nums[i])
                final_array.pop()
                
            return result
        
        candidates.sort()
        result, final_array = [], []
        n = len(candidates)
        result = combinationSumII(0, candidates, n, result, final_array, target)
        return result