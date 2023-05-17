for _ in range ( int ( input ( ) ) ) :
    n , m , r , var c = map ( int , input ( ) . split ( ) );
    System.out.println ( max ( abs ( n - r ) , r - 1 ) + max ( abs ( m - c ) , c - 1 ) );
