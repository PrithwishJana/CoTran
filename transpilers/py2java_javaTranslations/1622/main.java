public void getTotalXorOfSubarrayXors ( arr , N ) {
    var res = 0;
    for i in range ( 0 , N ) :
        freq = ( i + 1 ) * ( N - i );
        if (( freq % 2 == 1 )) {
            res = res ^ arr { i };
        }
     return res;
}
var arr = { 3 , 5 , 2 , 4 , 6 };
var N = len ( arr );
System.out.println ( getTotalXorOfSubarrayXors ( arr , N ) );
