class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=''.join(sorted(s))
        t=''.join(sorted(t))
        e=0
        for i in range(len(s)):
            if len(s)!=len(t):
                return False
            if s[i]==t[i]:
                e+=1
        if e==len(s):
            return True
        else:
            return False

