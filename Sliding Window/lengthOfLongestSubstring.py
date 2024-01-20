class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        i,j,result = 0,0,0
        hashset = set()

        while j<len(s):
            if s[j] not in hashset:
                hashset.add(s[j])
                j+=1
                result = max(result,len(hashset))
            else:
                hashset.remove(s[i])
                i+=1
        return result