import bisect.bisect_left as bl;
var n = int ( input ( ) );
var tlst = sorted ( { int ( input ( ) ) for _ in range ( n ) } );
var max_t = tlst { - 1 };
var divisors = { i for i in range ( 1 , max_t + 1 ) if max_t % i == 0 };
var ans = 0;
for (int t = 0; t < tlst.length; t++){
    var ind = bl ( divisors , t );
    ans += divisors { ind } - t;
}
System.out.println ( ans );
