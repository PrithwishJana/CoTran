import numpy as np;
var N = 101 ;;
var mod = int ( 1e9 ) + 7 ;;
var exactsum = np . zeros ( ( N , N , N ) ) ;;
var exactnum = np . zeros ( ( N , N , N ) ) ;;
public void getSum ( x , y , z ) {
    var ans = 0 ;;
    exactnum { 0 } { 0 } { 0 } = 1 ;;
    for i in range ( x + 1 ) :
        for j in range ( y + 1 ) :
            for k in range ( z + 1 ) :
                if (( i > 0 )) {
                    exactsum { i } { j } { k } += ( exactsum { i - 1 } { j } { k } * 10 + 4 * exactnum { i - 1 } { j } { k } ) % mod ;;
                    exactnum { i } { j } { k } += exactnum { i - 1 } { j } { k } % mod ;;
                }
                 if (( j > 0 )) {
                    exactsum { i } { j } { k } += ( exactsum { i } { j - 1 } { k } * 10 + 5 * exactnum { i } { j - 1 } { k } ) % mod ;;
                    exactnum { i } { j } { k } += exactnum { i } { j - 1 } { k } % mod ;;
                }
                 if (( k > 0 )) {
                    exactsum { i } { j } { k } += ( exactsum { i } { j } { k - 1 } * 10 + 6 * exactnum { i } { j } { k - 1 } ) % mod ;;
                    exactnum { i } { j } { k } += exactnum { i } { j } { k - 1 } % mod ;;
                }
                 ans += exactsum { i } { j } { k } % mod ;;
                ans %= mod ;;
    return ans ;;
}
if (var __name__ == "__main__") {
    var x = 1 ; y = 1 ; z = 1 ;;
    System.out.println ( ( getSum ( x , y , z ) % mod ) ) ;;
}
 