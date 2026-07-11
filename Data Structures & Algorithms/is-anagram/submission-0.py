class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # map s's chars to their counts
        s_map = {}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 1
        # compare
        for c in t:
            if c in s_map:
                if s_map[c] <= 1:
                    s_map.pop(c)
                else:
                    s_map[c] -= 1
            else:
                return False
        return len(s_map) == 0