class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = ""
        substringLength = float("infinity")
        charCountS = {}
        charCountT = {}
        for c in t:
            charCountS[c] = 0
            charCountT[c] = 1 + charCountT.get(c, 0)
        conditions = len(charCountT)
        conditionsMet = 0
        l = 0
        while l < len(s) and s[l] not in charCountT:
            l += 1
        for r in range(l, len(s)):
            if s[r] in charCountT:
                charCountS[s[r]] += 1
                if charCountS[s[r]] == charCountT[s[r]]:
                    conditionsMet += 1
                while charCountS[s[l]] > charCountT[s[l]]:
                    charCountS[s[l]] -= 1
                    # move l
                    l += 1
                    while l < r and s[l] not in charCountT:
                        l += 1
                if conditions == conditionsMet and substringLength > r - l + 1:
                    substring = s[l:r+1]
                    substringLength = r - l + 1
        return substring