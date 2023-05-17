for x in range ( int ( input ( ) ) ) :
    var a = int ( input ( ) );
    if (a > 59 and 360 % ( 180 - a ) == 0) {
        System.out.println ( 'YES' );
    }
     else{
        System.out.println ( "NO" );
    }
