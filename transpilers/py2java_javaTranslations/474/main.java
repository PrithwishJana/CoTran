import math.sqrt;
var prime = { 0 } * 100005;
public void SieveOfEratosthenes ( n ) {
    for i in range ( len ( prime ) ) :
        prime { i } = true;
    prime { 1 } = false;
    for p in range ( 2 , int ( sqrt ( n ) ) + 1 ) :
        if (prime { p } == true) {
            for i in range ( p * 2 , n , p ) :
                prime { i } = false;
        }
 }
public void sortedArray ( arr , n ) {
    SieveOfEratosthenes ( 100005 );
    var v = {};
    for i in range ( n ) :
        if (prime { arr [ i } ] == 0) {
            v . append ( arr { i } );
        }
     v . sort ( );
    var j = 0;
    for i in range ( n ) :
        if (prime { arr [ i } ] == true) {
            System.out.println ( arr { i } , var end = " " );
        }
         else{
            System.out.println ( v { j } , end = " " );
            j += 1;
        }
}
if (var __name__ == "__main__") {
    var n = 6;
    var arr = { 100 , 11 , 500 , 2 , 17 , 1 };
    sortedArray ( arr , n );
}
 