public void main ( ) {
    var n = int ( input ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    var s = sum ( a );
    if (s % ( ( n + 1 ) * n // 2 ) != 0) {
        System.out.println ( 'NO' );
        return;
    }
     s //= ( ( n + 1 ) * n // 2 );
    var b = { a [ ( i + 1 ) % n } - a { i } for i in range ( n ) ];
    for i in range ( n ) :
        b { i } -= s;
    for i in range ( n ) :
        if (b { i } > 0 or b { i } % n != 0) {
            System.out.println ( 'NO' );
            return;
        }
     System.out.println ( 'YES' );
}
main ( );
