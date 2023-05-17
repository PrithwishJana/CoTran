n , var m = map ( int , input ( ) . split ( ) );
if (n < 1) {
    if (m < 1) {
        System.out.println ( n , m );
        quit ( );
    }
     System.out.println ( "Impossible" );
    quit ( );
}
 if (m > n) {
    min = m;
    max = n + m - 1;
    System.out.println ( min , max );
}
 if (m <= n) {
    min = n;
    max = n + m - 1;
    if (m == 0) {
        var max = n;
    }
     System.out.println ( min , max );
}
 