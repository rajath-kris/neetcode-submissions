class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        test = set()

        for num in nums:
            if num not in test:
                test.add(num)
            else:
                return num