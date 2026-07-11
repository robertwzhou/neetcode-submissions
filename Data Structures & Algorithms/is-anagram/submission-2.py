class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for c in s:
            if c in s_dict:
                s_dict[c] += 1
            else:
                s_dict[c] = 1
        for c in t:
            if c not in s_dict:
                return False
            elif s_dict[c] == 1:
                del s_dict[c]
            else:
                s_dict[c] -= 1
        return len(s_dict) == 0