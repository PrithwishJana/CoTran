import math;
public void SumDivPrime ( A , n ) {
    var max_val = max ( A ) + 1;
    var prime = { true } * ( max_val + 1 );
    prime { 0 } = false;
    prime { 1 } = false;
    for p in range ( 2 , int ( math . sqrt ( max_val ) ) + 1 ) :
        if (prime { p } == true) {
            for i in range ( 2 * p , max_val + 1 , p ) :
                prime { i } = false;
        }
     var sum = 0;
    for i in range ( 0 , n ) :
        if (prime { A [ i } ]) {
            sum += A { i };
        }
     for i in range ( 0 , n ) :
        if (prime { A [ i } ] and sum % A { i } == 0) {
            System.out.println ( "YES" );
            return;
        }
     System.out.println ( "NO" );
}
var A = { 1 , 2 , 3 , 4 , 5 };
var n = len ( A );
SumDivPrime ( A , n );
