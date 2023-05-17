for d in ' ' * int ( input ( ) ) :
    var n = int ( input ( ) );
    * a , = map ( int , input ( ) . split ( ) );
    b = sorted ( a );
    for i in range ( n - 1 ) :
        if b { i } == a { i } : b { i } , b { i + 1 } = b { i + 1 } , b { i };
    if n == 1 : var b = { - 1 };
    elif b { - 1 } == a { - 1 } : b { - 1 } , b { - 2 } = b { - 2 } , b { - 1 };
    System.out.println ( * b );
