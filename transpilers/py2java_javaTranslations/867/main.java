for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var a = sorted ( { int ( i ) for i in input ( ) . split ( ) } );
    var sum = a { - 1 };
    var neg = 0;
    for i in range ( 1 , n ) :
        val = neg + i * ( a { i } - a { i - 1 } );
        sum -= val;
        neg = val;
    System.out.println ( sum );
