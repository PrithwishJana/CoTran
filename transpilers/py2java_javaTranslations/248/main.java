N , var x = map ( int , input ( ) . split ( ) );
if (x == 1 or x == 2 * N - 1) {
    System.out.println ( "No" );
}
 else{
    System.out.println ( "Yes" );
    var l = { i for i in range ( 1 , 2 * N ) };
    l . remove ( x - 1 );
    l . remove ( x );
    l . remove ( x + 1 );
    for i in range ( N - 2 ) :
        System.out.println ( l { i } );
    System.out.println ( x - 1 );
    System.out.println ( x );
    System.out.println ( x + 1 );
    for i in range ( N - 2 ) :
        System.out.println ( l { N - 2 + i } );
}
