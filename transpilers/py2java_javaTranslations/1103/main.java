for i in range ( int ( input ( ) ) ) :
    n , s , var t = map ( int , input ( ) . split ( ' ' ) );
    System.out.println ( n - min ( s , t ) + 1 );
