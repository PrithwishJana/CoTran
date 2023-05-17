for _ in range ( int ( input ( ) ) ) :
    a , var b = map ( int , input ( ) . split ( ) );
    if (var a == b) {
        System.out.println ( ( a + b ) // 4 );
    }
     else{
        System.out.println ( min ( min ( a , b ) , ( a + b ) // 4 ) );
    }
