var maxn = 1010;
var mod = 1000000007;
var comb = { [ 0 for i in range ( maxn ) } for i in range ( maxn ) ];
comb { 0 } { 0 } = 1;
for i in range ( 1 , maxn ) :
    comb { i } { 0 } = 1;
    for j in range ( 1 , i + 1 ) :
        comb { i } { j } = comb { i - 1 } { j } + comb { i - 1 } { j - 1 } % mod;
var k = int ( input ( ) );
var color = { int ( input ( ) ) for i in range ( k ) };
var res = 1;
total = 0;
for i in range ( k ) :
    res = ( res * comb { total + color [ i } - 1 ] { color [ i } - 1 ] ) % mod;
    total += color { i } % mod;
System.out.println ( res % mod );
