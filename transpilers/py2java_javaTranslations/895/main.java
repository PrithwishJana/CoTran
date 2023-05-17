public void f ( n ) {
    var a = set ( );
    var i = 2;
    while (i * i <= n) {
        while (n % i == 0) {
            a . add ( i );
            n //= i;
        }
         i += 1;
    }
     if n > 1 : a . add ( n );
    return a;
}
while (1) {
    a , var b = map ( int , input ( ) . split ( ) );
    if ( a | b ) == 0 : break;
    a , b = f ( a ) , f ( b );
    System.out.println ( "a" if 2 * max ( a ) - sum ( a ) > 2 * max ( b ) - sum ( b ) else "b" );
}
 