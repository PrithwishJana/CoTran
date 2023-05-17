for _ in range ( int ( input ( ) ) ) :
    a , b , var c = input ( ) . split ( " " );
    a , b , c = int ( a ) , int ( b ) , int ( c );
    a , b , c = sorted ( { a , b , c } );
    if (c - a <= 2) {
        System.out.println ( 0 );
    }
     else{
        System.out.println ( 2 * ( c - a - 2 ) );
    }
