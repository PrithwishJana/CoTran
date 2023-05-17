for i in range ( int ( input ( ) ) ) :
    var n = int ( input ( ) );
    if (( n <= 30 )) {
        System.out.println ( "NO" );
    }
     else{
        System.out.println ( "YES" );
        if (( n == 40 or n == 36 or n == 44 )) {
            System.out.println ( "6 10 15 " , n - 31 );
        }
         else{
            System.out.println ( "6 10 14" , n - 30 );
        }
    }
