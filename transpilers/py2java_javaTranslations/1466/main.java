while (1) {
    d , var e = map ( int , input ( ) . split ( ) );
    if (var d == 0) {
        break;
    }
     var data = {};
    for i in range ( 0 , 101 ) :
        for j in range ( 0 , 101 ) :
            data . append ( ( abs ( ( ( i * i + j * j ) ** 0.5 ) - e ) , i , j ) );
    for p in sorted ( data ) :
        if (p { 1 } + p { 2 } == d) {
            System.out.println ( p { 0 } );
            break;
        }
 }
 