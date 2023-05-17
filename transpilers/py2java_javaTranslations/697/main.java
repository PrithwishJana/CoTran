for i in range ( int ( input ( ) ) ) :
    var nm = input ( );
    nm = nm . split ( );
    var inp = input ( );
    inp = inp . split ( );
    for i in range ( int ( nm { 0 } ) ) :
        inp . append ( int ( inp { 0 } ) );
        inp . pop ( 0 );
    inp . sort ( );
    var sum1 = 0;
    for i in range ( int ( nm { 0 } ) ) :
        sum1 += max ( inp { i - 1 } , inp { i } );
    if (( sum1 + int ( nm { 0 } ) ) <= int ( nm { 1 } )) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
