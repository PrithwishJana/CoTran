var INF = 10 ** 20;
d , var n = map ( int , input ( ) . split ( ) );
var temp = { int ( input ( ) ) for i in range ( d ) };
temp . insert ( 0 , 0 );
var alst = {};
var blst = {};
var clst = {};
for i in range ( n ) :
    a , b , var c = map ( int , input ( ) . split ( ) );
    alst . append ( a );
    blst . append ( b );
    clst . append ( c );
var dp = { [ 0 } * n for i in range ( d + 1 ) ];
for i in range ( n ) :
    if (not ( alst { i } <= temp { 1 } <= blst { i } )) {
        dp { 1 } { i } = - INF;
    }
 for i in range ( 2 , d + 1 ) :
    var t = temp { i };
    for j in range ( n ) :
        if (alst { j } <= t <= blst { j }) {
            dp { i } { j } = max ( dp { i - 1 } { x } + abs ( clst { j } - clst { x } ) for x in range ( n ) );
        }
 System.out.println ( max ( dp { d } ) );
