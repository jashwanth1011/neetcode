class Solution {
    public int maxArea(int[] height) {
        if(height.length <2) return 0;
        int left =0, right = height.length -1, ans = Integer.MIN_VALUE;
        while(left<right){
            ans = Math.max(ans, (right-left)*Math.min(height[left],height[right]));
            if(height[left]>height[right]) right--;
            else left++;
        }
        return ans;
    }
}