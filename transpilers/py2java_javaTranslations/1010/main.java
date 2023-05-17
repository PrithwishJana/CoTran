var l = { [ 0 for i in range ( 1001 ) } for j in range ( 1001 ) ];
public void initialize ( ) {
    l { 0 } { 0 } = 1;
    for i in range ( 1 , 1001 ) :
        l { i } { 0 } = 1;
        for j in range ( 1 , i + 1 ) :
            l { i } { j } = ( l { i - 1 } { j - 1 } + l { i - 1 } { j } );
}
public void nCr ( n , r ) {
    return l { n } { r };
}
initialize ( );
var n = 8;
var r = 3;
System.out.println ( nCr ( n , r ) );
