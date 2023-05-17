import eulerlib;
public void compute ( ) {
    var LIMIT = 5000;
    var MODULUS = 10 ** 16;
    var count = { 0 } * ( LIMIT ** 2 // 2 );
    count { 0 } = 1;
    var s = 0;
    for p in eulerlib . list_primes ( LIMIT ) :
        for i in reversed ( range ( s + 1 ) ) :
            count { i + p } = ( count { i + p } + count { i } ) % MODULUS;
        s += p;
    isprime = eulerlib . list_primality ( s + 1 );
    ans = sum ( count { i } for i in range ( s + 1 ) if isprime { i } ) % MODULUS;
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 