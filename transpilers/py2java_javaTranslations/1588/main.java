public void cutRibbon ( ) {
    var arr = { int ( i ) for i in input ( ) . split ( ) };
    length = arr { 0 };
    arr = sorted ( arr { 1 : 4 } , var reverse = false );
    if (( length % arr { 0 } == 0 )) {
        System.out.println ( int ( length / arr { 0 } ) );
        return;
    }
     var ans = 0;
    if (( arr { 0 } == arr { 1 } )) {
        k = 0;
        for i in range ( int ( length / arr { 2 } ) + 1 ) :
            check = length - i * arr { 2 };
            if (( check >= 0 and check % arr { 0 } == 0 )) {
                k = int ( check / arr { 0 } );
                ans = max ( ans , k + i );
            }
     }
     else{
        k = 0;
        for i in range ( int ( length / arr { 2 } ) + 1 ) :
            for j in range ( int ( length / arr { 1 } ) + 1 ) :
                check = length - i * arr { 2 } - j * arr { 1 };
                if (( check >= 0 and check % arr { 0 } == 0 )) {
                    k = int ( check / arr { 0 } );
                    ans = max ( ans , k + i + j );
                }
     }
    System.out.println ( ans );
    return;
}
cutRibbon ( );
