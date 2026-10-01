class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if (len(s) > len(t)) or (t == "" and s!=""): 
        #     return False 
        # if (s=="" and t!=""):
        #     return True
        i = 0 
        for j in range(len(t)):
            if i == len(s):
                return True
            if t[j] == s[i]:
                i+=1
        return i == len(s)
        