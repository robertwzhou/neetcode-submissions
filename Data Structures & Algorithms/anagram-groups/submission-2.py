class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        because strs[i] is lowercase English letters only, a 26 char array suffices for each
        """
        # turn each str into 26 char count tuple
        def toCharCount(s: str) -> Tuple[int]:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord('a')] += 1
            return tuple(charCount)
        # group
        groups = {}
        for s in strs:
            charCount = toCharCount(s)
            if charCount not in groups:
                groups[charCount] = []
            groups[charCount].append(s)
        return list(groups.values())