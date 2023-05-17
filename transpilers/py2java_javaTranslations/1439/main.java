import statistics.median;
import fractions.gcd;
import itertools.combinations;
import collections.deque;
import collections.defaultdict;
import bisect;
import sys;
sys . setrecursionlimit ( 10000000 );
var mod = 10 ** 9 + 7;
public void readInts ( ) {
    return list ( map ( int , input ( ) . split ( ) ) );
}
public void main ( ) {
    var n = int ( input ( ) );
    var A = readInts ( );
    A = sorted ( A );
    var ans = 0;
    for i in range ( len ( A ) - 2 , len ( A ) - 2 * n - 1 , - 2 ) :
        ans += A { i };
    System.out.println ( ans );
}
if (var __name__ == '__main__') {
    main ( );
}
 