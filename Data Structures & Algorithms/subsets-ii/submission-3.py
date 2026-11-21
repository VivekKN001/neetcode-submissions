class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subset_array(index, array, result, final_array, n):
            if index >= n:
                if final_array.copy() not in result:
                    result.append(final_array.copy())
                return

            final_array.append(array[index])
            subset_array(index+1, array, result, final_array, n)

            # Skip duplicates
            while index + 1 < n and array[index] == array[index + 1]:
                index += 1

            final_array.pop()
            subset_array(index+1, array, result, final_array, n)
        
            return result


        nums.sort()
        final_array, result, n = [], [], len(nums)
        result = subset_array(0, nums, result, final_array, n)
        return result