class Solution:
    def romanToInt(self, s: str) -> int:
        x = { 
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
            }
        keys = list(x.keys())
        
        prevIndex = -1
        realNum = 0;
        for ind, r in enumerate(s):
            index = keys.index(r)
            charNum = x.get(r)
            
            nextIndex = -1
            if(ind != len(s) - 1):
                nextIndex = keys.index(s[ind+1])
            
            if(nextIndex != -1 and index < nextIndex):
                realNum -= charNum
            else:
                realNum += charNum
            
            prevIndex = index
        
        return realNum