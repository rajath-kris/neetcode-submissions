class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        duplicate2 = set(nums)

        if len(nums) > len(duplicate2):
            return True

        return False

        # for x in nums:
        #     if x not in duplicate2:
        #         duplicate2.append(x)
        #     else:
        #         return True
        
        # return False
            