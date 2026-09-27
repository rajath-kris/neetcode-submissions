from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result  = []
        counter = Counter(nums)
        most_common = counter.most_common(k)
        for x, y in most_common:
            result.append(x)
        return result
        
