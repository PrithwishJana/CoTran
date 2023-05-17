var t = int ( input ( ) );
for _ in range ( t ) :
    n , var k = map ( int , input ( ) . split ( ) );
    var a = list ( map ( int , input ( ) . split ( ) ) );
    var has = false;
    prop = n == 1;
    for i in range ( n ) :
        if a { i } == k : has = true;
        if (a { i } >= k and i > 0) {
            if a { i - 1 } >= k : var prop = true;
            if i > 1 and a { i - 2 } >= k : prop = true;
        }
     System.out.println ( "yes" if has and prop else "no" );
