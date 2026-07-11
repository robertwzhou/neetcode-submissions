class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            a = str(len(s)) + "L" + s
            encoded_string += a
        return encoded_string
    def decode(self, s: str) -> List[str]:
        def decode_one(i: int):
            j = i
            while s[j] != "L":
                j += 1
            length = int(s[i:j])
            return s[j+1 : j+1+length], j+1+length
        decoded_strs = []
        i = 0
        while i < len(s):
            decoded, i = decode_one(i)
            decoded_strs.append(decoded)
        return decoded_strs