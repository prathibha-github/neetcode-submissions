class Solution:

    def encode(self, strs: List[str]) -> str:
        result_list = []
        for string in strs:
            result_list.append(str(len(string)))
            result_list.append("#")
            result_list.append(string)
        return "".join(result_list)
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_len = int(s[i:j])
            i = j+1
            word = s[i:i+(word_len)]
            result.append(word)
            i = i + word_len
        return result