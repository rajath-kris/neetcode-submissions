from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1

            groups[tuple(count)].append(string)        
        return list(groups.values())