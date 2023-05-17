import eulerlib , fractions , itertools;
public void compute ( ) {
    var LIMIT = 10 ** 9;
    var ans = 0;
    for s in itertools . count ( 1 , 2 ) :
        if (s * s > ( LIMIT + 1 ) // 3) {
            break;
        }
         for t in range ( s - 2 , 0 , - 2 ) :
            if (fractions . gcd ( s , t ) == 1) {
                var a = s * t;
                var b = ( s * s - t * t ) // 2;
                var c = ( s * s + t * t ) // 2;
                if (a * var 2 == c - 1) {
                    p = c * 3 - 1;
                    if (p <= LIMIT) {
                        ans += p;
                    }
                 }
                 if (a * 2 == c + 1) {
                    p = c * 3 + 1;
                    if (p <= LIMIT) {
                        ans += p;
                    }
                 }
                 if (b * 2 == c - 1) {
                    p = c * 3 - 1;
                    if (p <= LIMIT) {
                        ans += p;
                    }
                 }
                 if (b * 2 == c + 1) {
                    var p = c * 3 + 1;
                    if (p <= LIMIT) {
                        ans += p;
                    }
                 }
             }
     return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 