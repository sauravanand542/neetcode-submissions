class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        deDupNums = set(nums)
        if len(nums)>len(deDupNums):  
            return True
        return False        

         