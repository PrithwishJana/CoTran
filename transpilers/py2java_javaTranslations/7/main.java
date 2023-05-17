import math.sqrt;
var MAX = 100000;
var prime = { true } * MAX;
var arr = {};
public void SieveOfEratosthenes ( ) {
    for p in range ( 2 , int ( sqrt ( MAX ) ) + 1 ) :
        if (prime { p } == true) {
            for i in range ( p * 2 , MAX , p ) :
                prime { i } = false;
        }
     for p in range ( 2 , MAX ) :
        if (prime { p }) {
            arr . append ( p );
        }
 }
public void isPrimorialPrime ( n ) {
    if (not prime { n }) {
        return false;
    }
     product , var i = 1 , 0;
    while (product < n) {
        product *= arr { i };
        if (product + var 1 == n or product - 1 == n) {
            return true;
        }
         i += 1;
    }
     return false;
}
if (var __name__ == "__main__") {
    SieveOfEratosthenes ( );
    var n = 31;
    if (( isPrimorialPrime ( n ) )) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
 