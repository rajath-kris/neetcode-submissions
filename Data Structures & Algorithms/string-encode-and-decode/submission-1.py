class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str_list = []
        for string in strs:
            l = len(string)
            encoded_str_list.append(str(l) + "#" +        string)

        return "".join(encoded_str_list)

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i<len(s):
            j = s.index("#", i)
            num = int(s[i:j])
            string = s[j+1: j+1+num]
            decoded_strings.append(string)
            i = j + 1 + num
        return decoded_strings
       


            

       