var n = int ( input ( ) );
var arr = list ( map ( int , input ( ) . split ( ) ) );
var diff = { abs ( arr [ i } - arr { i + 1 } ) for i in range ( n - 1 ) ];
var dp = { [ 0 , 0 , 0 } for _ in range ( n - 1 ) ];
dp { 0 } { 1 } = diff { 0 };
for i in range ( 1 , n - 1 ) :
    dp { i } { 0 } = max ( dp { i - 1 } { 0 } , dp { i - 1 } { 1 } , dp { i - 1 } { 2 } );
    dp { i } { 1 } = max ( dp { i - 1 } { 2 } + diff { i } , diff { i } );
    dp { i } { 2 } = dp { i - 1 } { 1 } - diff { i };
System.out.println ( max ( dp { n - 2 } { 0 } , dp { n - 2 } { 1 } , dp { n - 2 } { 2 } ) );
