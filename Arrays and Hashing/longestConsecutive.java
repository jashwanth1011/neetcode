class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length <2) return nums.length;
        int largetSeq = 0;
        HashSet<Integer> set = new HashSet();
        for(int num: nums){
            set.add(num);
        }
        
        for(int num: nums){
            if(!set.contains(num-1)){
                int currSeq = 1;
                while(set.contains(num+1)){
                    num++;
                    currSeq++;
                }
                largetSeq = Math.max(largetSeq, currSeq);
            }
            
        }
        return largetSeq;
    }
}