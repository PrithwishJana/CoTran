import sys.stdin , stdout;
var int_in = lambda : int ( stdin . readline ( ) );
var arr_in = lambda : { int ( x ) for x in stdin . readline ( ) . split ( ) };
var mat_in = lambda rows : { arr_in ( ) for _ in range ( rows ) };
var str_in = lambda : stdin . readline ( ) . strip ( );
var out = lambda o : stdout . write ( "{}\n" . format ( o ) );
arr_out = lambda o : out ( " " . join ( map ( str , o ) ) );
bool_out = lambda o : out ( "YES" if o else "NO" );
tests = lambda : range ( 1 , int_in ( ) + 1 );
case_out = lambda i , o : out ( "Case; //{}: {}" . format ( i , o ) )
public void solve ( n , k , m , a ) {
    var sa = sorted ( a );
    var prefix_sum = { 0 };
    for i in range ( n ) :
        prefix_sum . append ( sa { i } + prefix_sum { - 1 } );
    var best = 0;
    for i in range ( min ( n , m + 1 ) ) :
        total_power = prefix_sum { n } - prefix_sum { i };
        remaining_heros = len ( sa ) - i;
        max_that_can_be_added = min ( m - i , remaining_heros * k );
        best = max ( best , ( total_power + max_that_can_be_added ) / remaining_heros );
    return best;
}
if (var __name__ == "__main__") {
    n , k , var m = arr_in ( );
    var a = arr_in ( );
    out ( solve ( n , k , m , a ) );
}
 