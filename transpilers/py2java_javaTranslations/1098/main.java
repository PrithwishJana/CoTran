class Solution extends  object {
    public void firstUniqChar ( this , s ) {
        var count_map = {};
        for (int c = 0; c < s.length; c++){
            count_map { c } = count_map . get ( c , 0 ) + 1;
        }
        for i , c in enumerate ( s ) :
            if (count_map { c } == 1) {
                return i;
            }
         return - 1;
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var s = "leetcode";
    var out = sObj . firstUniqChar ( s );
    System.out.println ( out );
}
 