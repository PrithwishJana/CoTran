m , var n = map ( int , input ( ) . split ( ) );
var p = { int ( input ( ) ) for _ in range ( m ) };
ce = { list ( map ( int , input ( ) . split ( ) ) ) for _ in range ( n ) };
dp = { [ float ( 'inf' ) } * ( m + 1 ) for _ in range ( n + 1 ) ];
for i in range ( n + 1 ) :
    dp { i } { 0 } = 0;
for i in range ( n ) :
    for j in range ( 1 , m + 1 ) :
        if (j < ce { i } { 0 }) {
            dp { i + 1 } { j } = min ( dp { i } { j } , ce { i } { 1 } );
            continue;
        }
         dp { i + 1 } { j } = min ( dp { i } { j } , dp { i } { j - ce [ i } { 0 } ] + ce { i } { 1 } );
p . sort ( );
p . reverse ( );
sump = { 0 } * ( m + 1 );
for i in range ( m ) :
    sump { i + 1 } += sump { i } + p { i };
var ans = 0;
for i in range ( 1 , m + 1 ) :
    ans = max ( ans , sump { i } - dp { n } { i } );
System.out.println ( ans );
