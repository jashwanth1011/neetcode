class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) <3:
            return res

        nums = sorted(nums)

        for i in range(0, len(nums)-2):
            if i==0 or nums[i]!=nums[i-1]:
                l,r,target = i+1, len(nums)-1, -1*nums[i]
                while l<r:
                    if nums[l]+nums[r]==target:
                        #tempList = [nums[i],nums[l],nums[r]]
                        res.append([nums[i],nums[l],nums[r]])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r-=1
                        l+=1
                        r-=1
                    elif nums[l]+nums[r]<target:
                        l+=1
                    else:
                        r-=1
        return res
        