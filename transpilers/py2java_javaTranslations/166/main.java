var MAX = 50002 ;;
var primes = {};
public void sieve ( ) {
    var isPrime = { true } * ( MAX );
    var p = 2;
    while (p * p < MAX) {
        if (( isPrime { p } == true )) {
            for i in range ( p * 2 , MAX , p ) :
                isPrime { i } = false;
        }
         p += 1;
    }
     for p in range ( 2 , MAX ) :
        if (( isPrime { p } )) {
            primes . append ( p );
        }
 }
public void power ( x , y ) {
    var count = 0;
    var z = y;
    while (( x >= z )) {
        count += ( x // z );
        z *= y;
    }
     return count;
}
public void modMult ( a , b , mod ) {
    var res = 0;
    a = a % mod;
    while (( b > 0 )) {
        if (( b % 2 == 1 )) {
            res = ( res + a ) % mod;
        }
         var a = ( a * 2 ) % mod;
        b //= 2;
    }
     return res % mod;
}
public void countWays ( n , m ) {
    var ans = 1;
    for i in range ( 1 , len ( primes ) ) :
        powers = power ( n , primes { i } );
        if (( powers == 0 )) {
            break;
        }
         ans = modMult ( ans , powers + 1 , m ) % m;
    if (( ( ( ans - 1 ) % m ) < 0 )) {
        return ( ans - 1 + m ) % m;
    }
     else{
        return ( ans - 1 ) % m;
    }
}
if (var __name__ == "__main__") {
    sieve ( );
    var n = 4;
    var m = 7;
    System.out.println ( countWays ( n , m ) );
}
 