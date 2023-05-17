for _ in range ( int ( input ( ) ) ) :
    n , k , var z = map ( int , input ( ) . split ( ) );
    var a = { int ( x ) for x in input ( ) . split ( ) };
    var ans = 0;
    s = 0;
    mx = 0;
    for i in range ( k + 1 ) :
        if (i < n - 1) {
            mx = max ( mx , a { i } + a { i + 1 } );
        }
         s += a { i };
        if (i % 2 == k % 2) {
            tmp = ( k - i ) // 2;
            if (tmp <= z) {
                ans = max ( ans , s + mx * tmp );
            }
         }
     System.out.println ( ans );
