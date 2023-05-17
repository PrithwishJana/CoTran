import numpy as np;
var MOD = ( int ) ( 1e9 + 7 );
public void modulo_13 ( s , n ) {
    var dp = np . zeros ( ( n + 1 , 13 ) ) ;;
    dp { 0 } { 0 } = 1 ;;
    for i in range ( n ) :
        for j in range ( 10 ) :
            var nxt = ord ( s { i } ) - ord ( '0' ) ;;
            if (( s { i } == '?' )) {
                nxt = j ;;
            }
             for k in range ( 13 ) :
                var rem = ( 10 * k + nxt ) % 13 ;;
                dp { i + 1 } { rem } += dp { i } { k } ;;
                dp { i + 1 } { rem } %= MOD ;;
            if (( s { i } != '?' )) {
                break ;;
            }
     return int ( dp { n } { 5 } ) ;;
}
if (var __name__ == "__main__") {
    var s = "?44" ;;
    var n = len ( s ) ;;
    System.out.println ( modulo_13 ( s , n ) ) ;;
}
 