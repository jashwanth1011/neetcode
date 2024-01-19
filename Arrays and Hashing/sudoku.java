class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> set = new HashSet<>();
        for(int i = 0; i<board.length; i++){
            for(int j = 0; j<board[0].length; j++){
                if(board[i][j]!='.'){
                    String b = "("+board[i][j]+")";
                    if(!set.add(i+b) || !set.add(b+j) || !set.add(i/3 + b + j/3)){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}