public void solve ( ) {
    n , var i = map ( int , input ( ) . split ( ) );
    var ns = sorted ( { * map ( int , input ( ) . split ( ) ) } );
    var k = 1 << ( i * 8 // n );
    var lis = {};
    for i in range ( n - 1 ) :
        if ns { i } != ns { i + 1 } : lis . append ( i + 1 );
    lis . append ( n );
    System.out.println ( 0 if len ( lis ) <= k else n - max ( lis { i + k } - lis { i } for i in range ( len ( lis ) - k ) ) );
}
solve ( );
