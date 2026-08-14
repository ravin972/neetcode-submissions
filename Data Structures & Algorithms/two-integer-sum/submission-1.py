class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Now we are going with optimal:
        seen = {} #Map value -> Index

        for i, num in enumerate(nums):
            # for i in range(len(nums)):
            # num = nums[i]  # Extra line just to get the value
            # diff = target - num
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i