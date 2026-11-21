class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subset_array(index, array, result, final_array, n):
            if index >= n:
                result.append(final_array.copy())
                return

            final_array.append(array[index])
            subset_array(index+1, array, result, final_array, n)

            final_array.pop()
            subset_array(index+1, array, result, final_array, n)
        
            return result


        final_array, result, n = [], [], len(nums)
        result = subset_array(0, nums, result, final_array, n)
        return result