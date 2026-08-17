class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count freq of each number 
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Group numbers by frequences in buckets
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        # Collect top k elements from highest frequency to lowest
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res