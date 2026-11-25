class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in numdict:
                return [numdict[diff],i]
            numdict[n] = i
         