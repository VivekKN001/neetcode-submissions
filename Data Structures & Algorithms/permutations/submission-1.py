class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursivePermute(ds, nums, n, freq, result):
            if len(ds) == n:
                result.append(ds.copy())
                return
            for i in range(len(nums)):
                if not(freq[i]):
                    freq[i] = 1
                    ds.append(nums[i])
                    recursivePermute(ds, nums, n, freq, result)
                    ds.pop()
                    freq[i] = 0
            return result
        
        ds, result = [], []
        n = len(nums)
        freq = [0] * n
        result = recursivePermute(ds, nums, n, freq, result)
        return result