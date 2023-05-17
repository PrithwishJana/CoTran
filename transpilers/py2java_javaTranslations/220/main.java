for _ in range ( int ( input ( ) ) ) :
    a , var b = map ( int , input ( ) . split ( ) );
    a1 , var b1 = map ( int , input ( ) . split ( ) );
    if (max ( a , b ) == max ( a1 , b1 )) {
        if (min ( a , b ) + min ( a1 , b1 ) == max ( a , b )) {
            System.out.println ( 'YES' );
        }
         else{
            System.out.println ( 'NO' );
        }
    }
     else{
        System.out.println ( 'NO' );
    }
