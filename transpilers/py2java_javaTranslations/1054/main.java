for i in range ( int ( input ( ) ) ) :
    a , var b = map ( int , input ( ) . split ( ) );
    var z = sorted ( map ( int , input ( ) . split ( ) ) );
    z . reverse ( );
    q , var w = 0 , 0;
    for i in range ( a ) :
        q += z { i };
        if (q / ( i + 1 ) >= b) {
            w += 1;
        }
     System.out.println ( w );
