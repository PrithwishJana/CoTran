public void CeilIndex ( A , l , r , key ) {
    while (( r - l > 1 )) {
        var m = l + ( r - l ) // 2;
        if (( A { m } >= key )) {
            var r = m;
        }
         else{
            var l = m;
        }
    }
     return r;
}
public void LongestIncreasingSubsequenceLength ( A , size ) {
    var tailTable = { 0 for i in range ( size + 1 ) };
    var len = 0;
    tailTable { 0 } = A { 0 };
    len = 1;
    for i in range ( 1 , size ) :
        if (( A { i } < tailTable { 0 } )) {
            tailTable { 0 } = A { i };
        }
         else if (( A { i } > tailTable { len - 1 } )){
            tailTable { len } = A { i };
            len += 1;
        }
        else{
            tailTable { CeilIndex ( tailTable , - 1 , len - 1 , A [ i } ) ] = A { i };
        }
    return len;
}
var A = { 2 , 5 , 3 , 7 , 11 , 8 , 10 , 13 , 6 };
var n = len ( A );
System.out.println ( "Length of Longest Increasing Subsequence is " , LongestIncreasingSubsequenceLength ( A , n ) );
