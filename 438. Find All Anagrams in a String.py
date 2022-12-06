'''
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p_dict = {}
        s_dict = {}
        if len(p) > len(s): return res
        for i in range(len(p)):
            p_dict[p[i]] = 1 + p_dict.get(p[i], 0)
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)

        if s_dict == p_dict:
            res = [0]

        l = 0
        for r in range(len(p), len(s)):
            s_dict[s[r]] = 1 + s_dict.get(s[r], 0)
            s_dict[s[l]] -= 1

            if s_dict[s[l]] == 0:
                s_dict.pop(s[l])
            l += 1
            if s_dict == p_dict:
                res.append(l)
        return res