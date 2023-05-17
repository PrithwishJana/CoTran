class Solution {
    public void longestPalindrome ( this , s ) {
        var ans = 0;
        var char_map = {};
        for (int c = 0; c < s.length; c++){
            char_map { c } = char_map . get ( c , 0 ) + 1;
        }
        for c in list ( char_map . keys ( ) ) :
            if (char_map { c } % var 2 == 0) {
                ans += char_map . pop ( c );
            }
             else{
                ans += char_map { c } // 2 * 2;
            }
        if (len ( char_map ) != 0) {
            ans += 1;
        }
         return ans;
    }
}
if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var s = "abccccdd";
    var out = sObj . longestPalindrome ( s );
    System.out.println ( out );
}
 