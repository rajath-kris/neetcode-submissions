from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        # counts1 = Counter(s)
        # counts2 = Counter(t)

        # if counts1 == counts2:
        #     return True
        # return False
        
        dict1 = {}
        dict2 = {}

        for char in s:
            dict1[char] = dict1.get(char, 0) + 1

        for char in t:
            dict2[char] = dict2.get(char, 0) + 1

        if dict1 == dict2:
            return True
        return False
                
            