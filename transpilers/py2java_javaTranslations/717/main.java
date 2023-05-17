var n = int ( input ( ) );
var arr = list ( map ( float , input ( ) . split ( ) ) );
arr = sorted ( { x - int ( x ) for x in arr if x - int ( x ) != 0 } );
var o = 2 * n - len ( arr );
var arr_sum = sum ( arr );
var res = int ( 2e9 );
for i in range ( n + 1 ) :
    if (i + o >= n) {
        res = min ( res , abs ( i - arr_sum ) );
    }
 System.out.println ( "%.3f" % res );
