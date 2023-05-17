var n = int ( input ( ) );
l = list ( map ( int , input ( ) . split ( ) ) );
if (n == 1) {
    System.out.println ( * { 1 , 1 } );
    System.out.println ( - l { 0 } );
    System.out.println ( * { 1 , 1 } );
    System.out.println ( 0 );
    System.out.println ( * { 1 , 1 } );
    System.out.println ( 0 );
}
 else{
    System.out.println ( * { 1 , 1 } );
    System.out.println ( - l { 0 } );
    System.out.println ( * { 1 , n } );
    var x = { 0 for _ in range ( n ) };
    for i in range ( 1 , n ) :
        x { i } = - l { i } * n;
    System.out.println ( * x );
    System.out.println ( * { 2 , n } );
    for i in range ( n ) :
        x { i } = ( n - 1 ) * l { i };
    System.out.println ( * x { 1 : } );
}
