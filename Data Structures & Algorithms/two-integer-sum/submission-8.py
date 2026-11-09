class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        valIndex = {}

        for i,n in enumerate(nums):
            valIndex[n]=i

        for i,n in enumerate(nums):
            diff = target - nums[i]
            if diff in valIndex and valIndex[diff] != i:
                return [i, valIndex[diff]]
        