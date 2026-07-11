class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        # assume valid s
        decoded = []
        def read_str(start: int):
            # read until #, then get length
            i = start
            while s[i] != "#":
                i += 1
            length = int(s[start:i])
            # read string up to that length
            i += 1
            decoded.append(s[i:i+length])
            return i + length
        start = 0
        while start < len(s):
            start = read_str(start)
        return decoded