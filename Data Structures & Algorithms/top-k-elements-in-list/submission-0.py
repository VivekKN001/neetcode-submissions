class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1+count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        final_result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                final_result.append(n)
                if len(final_result)==k:
                    return final_result