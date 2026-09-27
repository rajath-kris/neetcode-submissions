from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counts = {}
        groups = {}
        result = []
        for string in strs:
            count = Counter(string)
            hashable_counts = tuple(sorted(count.items()))
            if hashable_counts not in groups:
                groups[hashable_counts] = []
            groups[hashable_counts].append(string)
        
        return list(groups.values())