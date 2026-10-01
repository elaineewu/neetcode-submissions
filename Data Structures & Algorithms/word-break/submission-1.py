class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashy={}
        def recur(s,i):

            if i== len(s):
                return True
            else:
                for j in wordDict:
                    if j == s[i:i+len(j)]:
                        if i+len(j) in hashy:
                            continue
                        if recur(s,i+len(j)):
                            return True
                        else:
                            hashy[i+len(j)]= False
                
                return False
                
        return recur(s,0)
        




        