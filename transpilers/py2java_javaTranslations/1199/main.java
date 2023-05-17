var N = int ( input ( ) );
var A = { int ( input ( ) ) * N + i for i in range ( N ) };
A . sort ( );
var cnt = 0;
for i in range ( N ) :
    var d = ( A { i } % N ) % 2;
    if (d % 2 != i % 2) {
        cnt += 1;
    }
 System.out.println ( cnt // 2 );
