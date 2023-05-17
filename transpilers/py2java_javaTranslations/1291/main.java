for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var v = list ( map ( int , input ( ) . split ( ) ) ) { : n };
    v . sort ( );
    System.out.println ( v { n - 1 } + v { n - 2 } );
