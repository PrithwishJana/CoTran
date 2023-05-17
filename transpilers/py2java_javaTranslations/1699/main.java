while (true) {
    var n = int ( input ( ) );
    if (n == 0) {
        break;
    }
     var s = list ( map ( int , input ( ) . split ( ) ) );
    if (max ( s ) < 2) {
        System.out.println ( 'NA' );
    }
     else{
        var t = s . count ( 0 );
        System.out.println ( n - t + 1 );
    }
}
 