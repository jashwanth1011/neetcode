class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        char[] charArray = s.toCharArray();
        int left = 0, right = charArray.length-1;

        while(left<right){
            if(!isValid(charArray[left])) left++;
            else if(!isValid(charArray[right])) right--;
            else{
                if(charArray[left]!=charArray[right]) return false;
                left++;
                right--;
            }
        }
        return true;
    }
    public boolean isValid(char c){
        if(Character.isDigit(c)||Character.isLetter(c)) return true;
        return false;
    }
}