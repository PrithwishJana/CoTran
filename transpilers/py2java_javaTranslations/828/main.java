var t = int ( input ( ) );
for _ in range ( t ) :
    a , var b = list ( map ( int , input ( ) . split ( ) ) );
    if (b == 1) {
        System.out.println ( "NO" );
    }
     else{
        System.out.println ( "YES" );
        System.out.println ( a , a * b , a * b + a );
    }
