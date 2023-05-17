var MAX = 250000;
var SQRT = 500;
var prime = { true } * MAX;
public void sieve ( ) {
    for i in range ( 2 , MAX , 2 ) : prime { i } = false;
    for i in range ( 3 , SQRT , 2 ) :
        if (prime { i }) {
            for j in range ( i * i , MAX , i ) : prime { j } = false;
        }
 }
sieve ( );
while (true) {
    var n = int ( input ( ) );
    if n == 0 : break;
    ans , m = 0 , n << 1;
    if n == 1 : ans += 1;
    var i = n + 1;
    if ( i & 1 ) == 0 : i += 1;
    while (i <= m) {
        if prime { i } : ans += 1;
        i += 2;
    }
     System.out.println ( ans );
}
 