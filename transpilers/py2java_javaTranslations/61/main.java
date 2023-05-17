var N = int ( input ( ) );
var A = list ( map ( int , input ( ) . split ( ) ) );
var a_to_i = { a : i for i , a in enumerate ( A , start = 1 ) };
var L = { i - 1 for i in range ( N + 2 ) };
var R = { i + 1 for i in range ( N + 2 ) };
var ans = 0;
for a in range ( N , 0 , - 1 ) :
    var i = a_to_i { a };
    ans += a * ( R { i } - i ) * ( i - L { i } );
    L { R [ i } ] = L { i };
    R { L [ i } ] = R { i };
System.out.println ( ans );
