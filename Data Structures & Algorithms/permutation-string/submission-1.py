class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        charCount1 = {}
        for c in s1:
            charCount1[c] = 1 + charCount1.get(c, 0)
        charCount2 = {}
        for i in range(len(s1)):
            charCount2[s2[i]] = 1 + charCount2.get(s2[i], 0)
        # fixed window of len(s1)
        i = 0
        def j():
            return i + len(s1)
        while j() <= len(s2):
            if charCount1 == charCount2:
                return True
            elif j() < len(s2) and s2[i] != s2[j()]:
                charCount2[s2[i]] -= 1
                charCount2[s2[j()]] = 1 + charCount2.get(s2[j()], 0)
                if charCount2[s2[i]] < 1:
                    charCount2.pop(s2[i])
            i += 1
        return False