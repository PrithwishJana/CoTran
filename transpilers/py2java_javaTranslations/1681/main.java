for pratyush in range ( int ( input ( ) ) ) :
    n , var r = map ( int , input ( ) . split ( ) );
    var a = min ( r , n - 1 );
    var ans = int ( ( a * ( a + 1 ) ) // 2 );
    if a != r : ans += 1;
    System.out.println ( ans );
