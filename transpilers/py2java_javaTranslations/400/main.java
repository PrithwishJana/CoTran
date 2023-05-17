var INF = 10 ** 20;
n , var m = map ( int , input ( ) . split ( ) );
var dist = {};
var weth = {};
for _ in range ( n ) :
    dist . append ( int ( input ( ) ) );
for _ in range ( m ) :
    weth . append ( int ( input ( ) ) );
var dp = { INF } * ( n + 1 );
dp { 0 } = 0;
for i in range ( m ) :
    for j in range ( n , 0 , - 1 ) :
        dp { j } = min ( dp { j } , dp { j - 1 } + dist { j - 1 } * weth { i } );
System.out.println ( dp { n } );
