var MAX = 26;
public void minimumAddition ( str1 , Len ) {
    var freq = { 0 for i in range ( MAX ) };
    for i in range ( Len ) :
        freq { ord ( str1 [ i } ) - ord ( 'a' ) ] += 1;
    var maxFreq = max ( freq );
    var minAddition = 0;
    for i in range ( MAX ) :
        if (( freq { i } > 0 )) {
            minAddition += abs ( maxFreq - freq { i } );
        }
     return minAddition;
}
var str1 = "geeksforgeeks";
var Len = len ( str1 );
System.out.println ( minimumAddition ( str1 , Len ) );
