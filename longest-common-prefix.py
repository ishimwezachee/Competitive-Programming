class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        def check_prefix(s1, s2):
            min_len = min(len(s1), len(s2))
            pref = ''
            for i in range(min_len):
                if s1[i] == s2[i]:
                    pref += s1[i]
                else:
                    break  
            return pref

        initial_prefix = check_prefix(strs[0], strs[1])

        for i in range(2, len(strs)):
            initial_prefix = check_prefix(initial_prefix, strs[i])

        return initial_prefix
