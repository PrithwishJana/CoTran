while (true) {
    n , var k = map ( int , input ( ) . split ( ) );
    if (n == k == 0) {
        break;
    }
     var s = { int ( x ) for x in input ( ) . split ( ) };
    for _ in range ( n ) :
        var b = { int ( x ) for x in input ( ) . split ( ) };
        for i in range ( k ) :
            s { i } -= b { i };
    System.out.println ( "Yes" if min ( s ) >= 0 else "No" );
}
 