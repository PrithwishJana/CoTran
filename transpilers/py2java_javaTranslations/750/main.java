for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var a = { int ( i ) for i in input ( ) . split ( ) } { : : - 1 };
    var minprice = { a [ 0 } ];
    for i in range ( 1 , n ) :
        minprice . append ( min ( minprice { i - 1 } , a { i } ) );
    var c = 0;
    for i in range ( n ) :
        c += a { i } > minprice { i };
    System.out.println ( c );
