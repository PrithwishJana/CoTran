var MAX = 26;
public void updateFreq ( strr , freq ) {
    var lenn = len ( strr );
    for i in range ( lenn ) :
        freq { ord ( strr [ i } ) - ord ( 'a' ) ] += 1;
}
public void maxCount ( strr , patt ) {
    var strrFreq = { 0 for i in range ( MAX ) };
    updateFreq ( strr , strrFreq );
    var pattFreq = { 0 for i in range ( MAX ) };
    updateFreq ( patt , pattFreq );
    var ans = 10 ** 9;
    for i in range ( MAX ) :
        if (( pattFreq { i } == 0 )) {
            continue;
        }
         ans = min ( ans , strrFreq { i } // pattFreq { i } );
    return ans;
}
var strr = "geeksforgeeks";
var patt = "geeks";
System.out.println ( maxCount ( strr , patt ) );
