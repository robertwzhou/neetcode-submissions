class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        longest = 0
        i = 0
        chars = {s[0]}
        for j in range(1, len(s)):
            while s[j] in chars:
                chars.remove(s[i])
                i += 1
            chars.add(s[j])
            longest = max(longest, j - i + 1)
        return longest
                