class Solution {
    public void xorQueries ( this , arr , queries ) {
        var pref = { 0 };
        for (int e = 0; e < arr.length; e++){
            pref . append ( e ^ pref { - 1 } );
        }
        var ans = {};
        for { l , r } in queries :
            ans . append ( pref { r + 1 } ^ pref { l } );
        return ans;
    }
}
if (var __name__ == "__main__") {
    var sObj = Solution ( );
    var arr = { 1 , 3 , 4 , 8 };
    var queries = { [ 0 , 1 } , { 1 , 2 } , { 0 , 3 } , { 3 , 3 } ];
    var out = sObj . xorQueries ( arr , queries );
    System.out.println ( out );
}
 