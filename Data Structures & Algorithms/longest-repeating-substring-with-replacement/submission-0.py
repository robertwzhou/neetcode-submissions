class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        charCount = {}
        maxFrequency = 0
        l = 0
        for r, c in enumerate(s):
            charCount[c] = 1 + charCount.get(c, 0)
            maxFrequency = max(maxFrequency, charCount[c])
            while r - l + 1 - maxFrequency > k:
                charCount[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
        return maxLength