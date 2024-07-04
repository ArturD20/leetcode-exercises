class Solution(object):
    def groupAnagrams(self, strs):
        
        res = defaultdict(list) #dzięki temu nie musimy robić warunków na puste tablice lub z jednym elementem
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1 #ASCII użyte do indeksowania np. "a" to 0 bo np. ASCII A to 80 więc 80 - 80 = 0 b to 1 bo b ma 81 czyli 81 - 80 = 1 itd.

            res[tuple(count)].append(word) # trzeba na tuple bo array nie moze być kluczem w hashmapie

        return res.values()
        