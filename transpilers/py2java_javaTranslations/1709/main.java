while (true) {
    n , t , L , var b = ( int ( s ) for s in input ( ) . split ( ) );
    if (( n , t , L , b ) == ( 0 , 0 , 0 , 0 )) {
        break;
    }
     var loses = { int ( input ( ) ) for i in range ( L ) };
    var backs = { int ( input ( ) ) for i in range ( b ) };
    var dp = { [ 0. } * n + { 1. } for i in range ( 3 ) ];
    var stops = list ( range ( n + 1 ) ) + list ( reversed ( range ( n - 5 , n ) ) );
    for i in reversed ( range ( t ) ) :
        for j in range ( n ) :
            dp { i % 3 } { j } = sum ( dp { ( i + 2 ) % 3 } { d } if d in loses else dp { ( i + 1 ) % 3 } { 0 } if d in backs else dp { ( i + 1 ) % 3 } { d } for d in stops { j + 1 : j + 7 } ) / 6;
    System.out.println ( '{:.6f}' . format ( dp { 0 } { 0 } ) );
}
 