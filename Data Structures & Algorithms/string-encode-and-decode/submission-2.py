class Solution:

    def encode(self, strs: List[str]) -> str:
        # len of str, delimiter, str
        s = ""
        for e in strs:
            s += str(len(e)) + " " + e
        return s
        
    def decode(self, s: str) -> List[str]:
        decoded = []
        loc = 0
        def decoding(loc: int) -> Tuple[str, int]:
            # parse length
            i = loc
            while s[i] != " ":
                i += 1
            length = int(s[loc: i])
            # parse word
            i += 1
            return s[i: i + length], i + length
        while loc < len(s):
            word, loc = decoding(loc)
            decoded.append(word)
        return decoded