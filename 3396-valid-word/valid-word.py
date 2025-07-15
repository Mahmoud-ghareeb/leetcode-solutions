import string

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        
        punc = string.digits + string.ascii_letters
        vowels = "aeoiu"
        
        v = False
        c = False
        for i in word:
            if i not in punc: return False
            if i.lower() in vowels: v = True
            elif i not in string.digits: c=True

        if v and c:
            return True

        return False
