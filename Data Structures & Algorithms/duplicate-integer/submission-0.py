class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       length = len(nums) 
       count = {}
       for i in range(length):
            curr = nums[i]
            if curr in count:
                return True 

            else: 
                count[curr] = 1

        
       return False