var N = int ( input ( ) );
var MOD = 10 ** 9 + 7;
fact , fact_inv , var inv = { 0 } * ( N + 1 ) , { 0 } * ( N + 1 ) , { 0 } * ( N + 1 );
public void main ( ) {
    var a = list ( map ( int , input ( ) . split ( ) ) );
    fact { 0 } = 1;
    for i in range ( 1 , N + 1 ) :
        fact { i } = fact { i - 1 } * i % MOD;
    fact_inv { N } = pow ( fact { N } , MOD - 2 , MOD );
    for i in range ( N - 1 , 0 , - 1 ) :
        fact_inv { i } = fact_inv { i + 1 } * ( i + 1 ) % MOD;
    for i in range ( 1 , N + 1 ) :
        inv { i } = fact_inv { i } * fact { i - 1 } % MOD;
    b , var s = { 0 } * N , { 0 } * ( N + 1 );
    for i in range ( 1 , N + 1 ) :
        s { i } = ( s { i - 1 } + inv { i } ) % MOD;
    for i in range ( N ) :
        b { i } = ( s { i + 1 } + s { N - i } - 1 ) % MOD;
    ans = 0;
    for i in range ( N ) :
        ans = ( ans + a { i } * b { i } ) % MOD;
    ans = ans * fact { N } % MOD;
    System.out.println ( ans );
}
if (var __name__ == '__main__') {
    main ( );
}
 