class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            s = str(sorted(string))
            if s in groups:
                groups[s].append(string)
            else:
                groups[s] = [string]
        return [v for k, v in groups.items()]