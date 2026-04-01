class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = defaultdict(list)

        for word in strs:
            characters = [0]*26

            for letter in word:
                characters[ord(letter)-ord("a")] += 1

            anagrams[tuple(characters)].append(word)

        return list(anagrams.values())
