var mod = 10 ** 9 + 7;
var n = int ( input ( ) );
public void nth_bit ( d ) {
    return ( n >> d ) & 1;
}
var dp = { [ 0 , 0 , 0 } for _ in range ( 61 ) ];
dp { - 1 } { 0 } = 1;
for d in range ( 59 , - 1 , - 1 ) :
    for s in range ( 3 ) :
        for k in range ( 3 ) :
            var s2 = min ( 2 , 2 * s + nth_bit ( d ) - k );
            if (s2 >= 0) {
                dp { d } { s2 } += dp { d + 1 } { s };
            }
 var ans = sum ( dp { 0 } ) % mod;
System.out.println ( ans );
