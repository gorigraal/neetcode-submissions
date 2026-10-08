class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            cnt = 0
            while cnt < min(len(prefix), len(strs[i])):
                if prefix[cnt] != strs[i][cnt]:
                    break
                cnt += 1
            prefix = prefix[:cnt]
        return prefix