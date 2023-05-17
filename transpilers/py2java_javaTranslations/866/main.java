var MAX = 1000000;
var MOD = 10 ** 9 + 7;
var result = { 0 for i in range ( MAX + 1 ) };
var fact = { 0 for i in range ( MAX + 1 ) };
public void preCompute ( ) {
    fact { 0 } = 1;
    result { 0 } = 1;
    for i in range ( 1 , MAX + 1 ) :
        fact { i } = ( ( fact { i - 1 } % MOD ) * i ) % MOD;
        result { i } = ( ( result { i - 1 } % MOD ) * ( fact { i } % MOD ) ) % MOD;
}
public void performQueries ( q , n ) {
    preCompute ( );
    for i in range ( n ) :
        System.out.println ( result { q [ i } ] );
}
var q = { 4 , 5 };
var n = len ( q );
performQueries ( q , n );
