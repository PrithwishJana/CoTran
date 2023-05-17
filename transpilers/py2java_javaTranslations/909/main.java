var n = int ( input ( ) );
n += 1;
for _ in range ( int ( input ( ) ) ) :
    a , var b = map ( int , input ( ) . split ( ) );
    System.out.println ( ( min ( min ( a , n - a ) , min ( b , n - b ) ) - 1 ) % 3 + 1 );
