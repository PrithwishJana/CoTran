var t = int ( input ( ) );
for _ in range ( t ) :
    n , var m = list ( map ( int , input ( ) . split ( ) ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    var s = 0;
    if (sum ( a ) == m) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
