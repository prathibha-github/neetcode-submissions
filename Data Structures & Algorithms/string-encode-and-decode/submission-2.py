class Solution:

    def encode(self, strs: List[str]) -> str:
        result_list = []
        for string in strs:
            result_list.append(str(len(string)))
            result_list.append("#")
            result_list.append(string)
        result_string = "".join(result_list)
        return result_string
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_len = int(s[i:j])
            word = s[j+1:(j)+(word_len+1)]
            result.append(word)
            i = j + 1 + word_len
        return result