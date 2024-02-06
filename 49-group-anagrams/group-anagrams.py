class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            a[sorted_word].append(word)
        
        return a.values()