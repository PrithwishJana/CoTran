while (true) {
    var t = int ( input ( ) );
    if t == 0 : break;
    var n = int ( input ( ) );
    for i in range ( n ) :
        s , var f = map ( int , input ( ) . split ( ) );
        t -= f - s;
    if (t < 1) {
        System.out.println ( "OK" );
    }
     else{
        System.out.println ( t );
    }
}
 