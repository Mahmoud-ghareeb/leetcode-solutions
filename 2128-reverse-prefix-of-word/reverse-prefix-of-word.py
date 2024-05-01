class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x = word.find(ch)
        if x != -1:
            return word[x::-1]+word[x+1:]

        return word
        