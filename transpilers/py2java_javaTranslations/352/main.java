import math.sqrt;
var MAX = 100000;
var prime = { true } * MAX;
public void sieve ( ) {
    for p in range ( 2 , int ( sqrt ( MAX ) ) + 1 ) :
        if (prime { p } == true) {
            for i in range ( p * 2 , MAX , p ) :
                prime { i } = false;
        }
 }
public void System.out.printlnPrimeQuad ( n ) {
    for i in range ( n - 7 ) :
        if (( prime { i } and prime { i + 2 } and prime { i + 6 } and prime { i + 8 } )) {
            System.out.println ( i , i + 2 , i + 6 , i + 8 );
        }
 }
if (var __name__ == "__main__") {
    sieve ( );
    var n = 20;
    System.out.printlnPrimeQuad ( 20 );
}
 