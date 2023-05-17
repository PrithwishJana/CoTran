for _ in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    var l = list ( map ( int , input ( ) . split ( ) ) );
    var d = {};
    var f = 0;
    for i in range ( n ) :
        x = ( i + l { i } ) % n;
        if (x in d) {
            f = 1;
            break;
        }
         else{
            d { x } = 1;
        }
    if (f == 1) {
        System.out.println ( 'NO' );
    }
     else{
        System.out.println ( 'YES' );
    }
