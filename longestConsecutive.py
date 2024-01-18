class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()
        longestSeq = 0

        for num in nums:
            unique.add(num)
        
        for num in nums:
            if num-1 not in unique:
                currSeq=1
                while num+1 in unique:
                    num += 1
                    currSeq += 1
                longestSeq = max(longestSeq, currSeq)
        return longestSeq
