class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # duplicate = Set()
        duplicate2 = []
        for x in nums:
            if x not in duplicate2:
                duplicate2.append(x)
            else:
                return True
        
        return False
            