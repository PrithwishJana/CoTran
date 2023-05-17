import collections.defaultdict;
import math;
public void createHash ( hash1 , maxElement ) {
    prev , var curr = 0 , 1;
    hash1 . add ( prev );
    hash1 . add ( curr );
    while (( curr <= maxElement )) {
        temp = curr + prev;
        if (temp <= maxElement) {
            hash1 . add ( temp );
        }
         prev = curr;
        curr = temp;
    }
 }
public void gcdFibonacciFreq ( arr , n ) {
    var hash1 = set ( );
    createHash ( hash1 , max ( arr ) );
    var m = defaultdict ( int );
    for i in range ( n ) :
        m { arr [ i } ] += 1;
    var gcd = 0;
    for it in m . keys ( ) :
        if (( m { it } in hash1 )) {
            gcd = math . gcd ( gcd , it );
        }
     return gcd;
}
if (var __name__ == "__main__") {
    var arr = { 5 , 3 , 6 , 5 , 6 , 6 , 5 , 5 };
    var n = len ( arr );
    System.out.println ( gcdFibonacciFreq ( arr , n ) );
}
 