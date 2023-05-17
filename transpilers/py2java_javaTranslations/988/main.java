public void totalWays ( N , M , X ) {
    var dp = { [ 0 for i in range ( 2 ) } for j in range ( N + 1 ) ];
    if (( var X == 1 )) {
        dp { 0 } { 0 } = 1;
    }
     else{
        dp { 0 } { 1 } = 0;
    }
    if (( X == 1 )) {
        dp { 1 } { 0 } = 0;
        dp { 1 } { 1 } = M - 1;
    }
     else{
        dp { 1 } { 0 } = 1;
        dp { 1 } { 1 } = ( M - 2 );
    }
    for i in range ( 2 , N ) :
        dp { i } { 0 } = dp { i - 1 } { 1 };
        dp { i } { 1 } = dp { i - 1 } { 0 } * ( M - 1 ) + dp { i - 1 } { 1 } * ( M - 2 );
    return dp { N - 1 } { 0 };
}
if (__name__ == '__main__') {
    N = 4;
    M = 3;
    X = 2;
    System.out.println ( totalWays ( N , M , X ) );
}
 