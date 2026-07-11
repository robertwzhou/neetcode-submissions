class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        charIndex = {}
        l = 0
        for r, c in enumerate(s):
            if c in charIndex:
                l = max(l, charIndex[c] + 1)
            charIndex[c] = r
            maxLength = max(maxLength, r - l + 1)
        return maxLength