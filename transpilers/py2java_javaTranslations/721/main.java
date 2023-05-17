import math.sqrt;
var MAX = 1005;
public void SieveOfEratosthenes ( primes ) {
    var prime = { true for i in range ( MAX ) };
    for p in range ( 2 , int ( sqrt ( MAX ) ) + 1 , 1 ) :
        if (( prime { p } == true )) {
            for i in range ( p * 2 , MAX , p ) :
                prime { i } = false;
        }
     for p in range ( 2 , MAX , 1 ) :
        if (( prime { p } )) {
            primes . append ( p );
        }
     return primes;
}
public void minimumSquareFreeDivisors ( N ) {
    prime = {};
    var primes = {};
    primes = SieveOfEratosthenes ( prime );
    var max_count = 0;
    i = 0;
    while (( len ( primes ) and primes { i } * primes { i } <= N )) {
        if (( N % primes { i } == 0 )) {
            tmp = 0;
            while (( N % primes { i } == 0 )) {
                tmp += 1;
                N /= primes { i };
            }
             max_count = max ( max_count , tmp );
        }
         i += 1;
    }
     if (( max_count == 0 )) {
        max_count = 1;
     }
     return max_count;
}
if (var __name__ == '__main__') {
    var N = 24;
    System.out.println ( "Minimum Number of Square Free Divisors is" , minimumSquareFreeDivisors ( N ) );
    N = 6;
    System.out.println ( "Minimum Number of Square Free Divisors is" , minimumSquareFreeDivisors ( N ) );
}
 