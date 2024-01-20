class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        
        l,r,ans = 0, len(height)-1, 0
        while l<r:
            ans = max(ans, (r-l)*min(height[l],height[r]))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return ans
        