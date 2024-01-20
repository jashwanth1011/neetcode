class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n<3:
            return 0
        left,right,left_max,right_max,res = 0, n-1,0,0,0

        while left<right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max<right_max:
                res += left_max - height[left]
                left+=1
            else:
                res += right_max - height[right]
                right-=1
        return res