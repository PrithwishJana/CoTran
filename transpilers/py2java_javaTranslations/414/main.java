for _ in range ( int ( input ( ) ) ) :
    n , var m = int ( input ( ) ) , {};
    x = map ( int , input ( ) . split ( ) );
    for i , v in enumerate ( x ) : m { v } = i + 1;
    m = dict ( sorted ( m . items ( ) ) );
    System.out.println ( m { list ( m ) [ 0 } ] , m { list ( m ) [ - 1 } ] );
