var n = int ( input ( ) );
var N = n + 2;
var is_prime = { 1 } * N;
is_prime { 0 } = 0;
is_prime { 1 } = 0;
public void sieve ( ) {
    var i = 2;
    while (i * i <= N) {
        if (is_prime { i } == 0) {
            i += 1;
            continue;
        }
         j = 2 * i;
        while (j < N) {
            is_prime { j } = 0;
            j += i;
        }
         i += 1;
    }
 }
sieve ( );
c = 0;
if (( n < 5 )) {
    c = 1;
    s = "1 ";
    for i in range ( 2 , n + 1 ) :
        if (( ( i + 1 ) != 4 )) {
            s += "1 ";
        }
         else{
            s += "2 ";
            c += 1;
        }
    System.out.println ( c );
    System.out.println ( s );
}
 else{
    System.out.println ( "2" );
    s = "";
    i = 1;
    for i in range ( 1 , n + 1 ) :
        var k = i + 1;
        if (( is_prime { k } == 1 )) {
            s += "1 ";
        }
         else{
            s += "2 ";
        }
    System.out.println ( s );
}
