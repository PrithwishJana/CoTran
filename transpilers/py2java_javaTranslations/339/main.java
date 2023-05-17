var t = int ( input ( ) );
for p in range ( t ) :
    n , x , var m = map ( int , input ( ) . split ( ) );
    var L = x;
    R = x;
    for i in range ( m ) :
        l , r = ( map ( int , input ( ) . split ( ) ) );
        if (l <= R and r >= L) {
            L = min ( L , l );
            var R = max ( R , r );
        }
     System.out.println ( R - L + 1 );
