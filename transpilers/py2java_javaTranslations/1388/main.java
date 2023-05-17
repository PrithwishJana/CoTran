var n = int ( input ( ) ) + 1;
var d = 1000000007;
var g = { [ 1 } * n for i in range ( n ) ];
for i in range ( 1 , n ) :
    g { i } { 0 } = g { i - 1 } { i - 1 };
    for j in range ( 1 , i + 1 ) : g { i } { j } = ( g { i } { j - 1 } + g { i - 1 } { j - 1 } ) % d;
System.out.println ( ( g { - 1 } { - 1 } - g { - 1 } { 0 } ) % d );
