class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCharDict = {}
        
        totalRead = 0;
        for char in ransomNote:
            if ransomCharDict.get(char):
                continue
            else:
                charC = ransomNote.count(char)
                totalRead += charC
                ransomCharDict[char] = charC
                
            if(len(ransomNote) == totalRead):
                break
                
        for x in ransomCharDict:
            if(magazine.count(x) < ransomCharDict.get(x)):
                return False
            
        return True