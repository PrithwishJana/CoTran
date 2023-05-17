import math;
public void maximumXOR ( n , l , r ) {
    var x = 0;
    for i in range ( int ( math . log2 ( r ) ) , - 1 , - 1 ) :
        if (( n & ( 1 << i ) )) {
            if (( x > r ) or ( x + ( 1 << i ) - 1 < l )) {
                x ^= ( 1 << i );
            }
         }
         else{
            if (( x ^ ( 1 << i ) ) <= r) {
                x ^= ( 1 << i );
            }
         }
    return n ^ x;
}
var n = 7;
var l = 2;
var r = 23;
System.out.println ( "The output is" , maximumXOR ( n , l , r ) );
