import math.gcd , sqrt;
var prime = { true } * 100001;
public void SieveOfEratosthenes ( ) {
    prime { 0 } = false;
    prime { 1 } = false;
    for p in range ( 2 , int ( sqrt ( 100001 ) ) + 1 ) :
        if (prime { p } == true) {
            for i in range ( p ** 2 , 100001 , p ) :
                prime { i } = false;
        }
 }
public void common_prime ( a , b ) {
    var __gcd = gcd ( a , b );
    for i in range ( 2 , __gcd + 1 ) :
        if (prime { i } and __gcd % var i == 0) {
            System.out.println ( i , var end = " " );
        }
 }
if (var __name__ == "__main__") {
    SieveOfEratosthenes ( );
    a , var b = 6 , 12;
    common_prime ( a , b );
}
 