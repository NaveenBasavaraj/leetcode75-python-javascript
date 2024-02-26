from collections import defaultdict
class Anagrams:
    def group_anagrams(self, words):
        
        ans = defaultdict(list)
        
        for word in words:
            count = [0]*26
            for chr in word:
                count[ord(chr)-ord('a')] += 1
            ans[tuple(count)].append(word)
        return ans.values()
        
    def is_anagram(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        count_s1, count_s2 = {}, {}
        
        for i in range(len(s1)):
            count_s1[s1[i]] = 1 + count_s1.get(s1[i], 0)
            count_s2[s2[i]] = 1 + count_s2.get(s2[i], 0)
        
        # return count_s1 == count_s2
        
        for k in count_s1.keys():
            if  count_s1[k] != count_s1[k]:
                return False
        
        return True


if __name__ == "__main__":
    res = Anagrams()
    print(res.is_anagram("tea","ate"))
    print(res.group_anagrams(["care","tea","nap","ate","pan","eat", "race"]))