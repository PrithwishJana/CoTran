import itertools.combinations;
N , var K = map ( int , input ( ) . split ( ) );
var P = { tuple ( map ( int , input ( ) . split ( ) ) ) for _ in range ( N ) };
var ans = 10 ** 18 * 5;
for x in combinations ( range ( N ) , 2 ) :
    u = max ( P { x [ 0 } ] { 0 } , P { x [ 1 } ] { 0 } );
    d = min ( P { x [ 0 } ] { 0 } , P { x [ 1 } ] { 0 } );
    for y in combinations ( range ( N ) , 2 ) :
        r = max ( P { y [ 0 } ] { 1 } , P { y [ 1 } ] { 1 } );
        l = min ( P { y [ 0 } ] { 1 } , P { y [ 1 } ] { 1 } );
        count = 0;
        for i in range ( N ) :
            if (d <= P { i } { 0 } <= u and l <= P { i } { 1 } <= r) {
                count += 1;
            }
         if (count >= K) {
            ans = min ( ans , ( u - d ) * ( r - l ) );
        }
 System.out.println ( ans );
