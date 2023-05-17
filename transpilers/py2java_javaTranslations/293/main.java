class Solution extends  object {
    public void numJewelsInStones ( this , J , S ) {
        if (len ( J ) == 0 or len ( S ) == 0) {
            return 0;
        }
         var j_set = set ( J );
        var ans = 0;
        for (int c = 0; c < S.length; c++){
            if (c in j_set) {
                ans += 1;
            }
        }
         return ans;
    }
}

if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var J = "aA";
    var S = "aAAbbbb";
    var out = sObj . numJewelsInStones ( J , S );
    System.out.println ( out );
}
 