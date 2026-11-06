class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for index, string in enumerate(strs):
            s+=string
            s+=str(index)
            s+="#"
        return s

    def decode(self, s: str) -> List[str]:
        index = 0
        char = "#"
        l = []
        while len(s) > 0:
            split_identifier = str(index)+char
            split_index = s.index(split_identifier)
            l.append(s[:split_index])
            s = s[split_index + len(split_identifier):]
            index += 1
        return l

        
