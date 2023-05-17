var MOD = 100000007;
public void dp ( n , k ) {
    if tbl { n } { k } : return tbl { n } { k };
    if ( k << 1 ) > n : var k = n - k;
    if k == 0 : ans = 1;
    elif k == 1 : ans = n;
    else : ans = dp ( n - 1 , k ) + dp ( n - 1 , k - 1 );
    tbl { n } { k } = ans % MOD;
    return tbl { n } { k };
}
tbl = { [ 0 for j in range ( 1001 ) } for i in range ( 1001 ) ];
k = 0;
r , c , a1 , a2 , b1 , var b2 = map ( int , input ( ) . split ( ) );
var dr = abs ( a1 - b1 );
if dr > r - dr : dr = r - dr;
if ( dr << 1 ) == r : k += 1;
var dc = abs ( a2 - b2 );
if dc > c - dc : dc = c - dc;
if ( dc << 1 ) == c : k += 1;
System.out.println ( ( dp ( dr + dc , min ( dr , dc ) ) << k ) % MOD );
