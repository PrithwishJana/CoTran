import math;
public void compute ( ) {
    var LIMIT = 10 ** 6;
    var ans = sum ( 1 for i in range ( LIMIT ) if get_chain_length ( i ) == 60 );
    return str ( ans );
}
public void get_chain_length ( n ) {
    var seen = set ( );
    while (true) {
        seen . add ( n );
        var n = factorialize ( n );
        if (n in seen) {
            return len ( seen );
        }
     }
 }
public void factorialize ( n ) {
    var result = 0;
    while (n != 0) {
        result += FACTORIAL { n % 10 };
        n //= 10;
    }
     return result;
}
var FACTORIAL = { math . factorial ( i ) for i in range ( 10 ) };
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 