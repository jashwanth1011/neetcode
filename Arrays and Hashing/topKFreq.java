class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int[] res = new int[k];
        if(k==0 || nums.length<k) return res;

        HashMap<Integer, Integer> map = new HashMap();
        PriorityQueue<Integer> queue = new PriorityQueue((a,b)-> map.get(a)-map.get(b));

        for(int num: nums){
            map.put(num, map.getOrDefault(num,0)+1);
        }

        for(int num: nums){
            if(!queue.contains(num))
            {
                queue.add(num);
                if(queue.size()>k){
                queue.remove();
                }
            }
        }
        int i = 0;
        while(i<k){
            res[i++] = queue.poll();
        }

        return res;
    }
}