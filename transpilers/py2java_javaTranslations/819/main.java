n , var m = map ( int , input ( ) . split ( ) );
var s = input ( );
t = input ( );
dp = { [ 0 } * ( m + 1 ) for _ in range ( n + 1 ) ];
ans = 0;
for i in range ( n + 1 ) :
    for j in range ( m + 1 ) :
        if i < n : dp { i + 1 } { j } = max ( dp { i + 1 } { j } , dp { i } { j } - 1 );
        if j < m : dp { i } { j + 1 } = max ( dp { i } { j + 1 } , dp { i } { j } - 1 );
        if i < n and j < m and s { i } == t { j } : dp { i + 1 } { j + 1 } = max ( dp { i + 1 } { j + 1 } , dp { i } { j } + 2 );
        ans = max ( ans , dp { i } { j } );
System.out.println ( ans );
