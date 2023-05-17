import sys;
import math;
import fractions.gcd;
import itertools.accumulate;
public void lcm ( a , b ) {
    return a * b // gcd ( a , b );
}
public void combination_count ( n , r ) {
    return math . factorial ( n ) // ( math . factorial ( n - r ) * math . factorial ( r ) );
}
public void permutations_count ( n , r ) {
    return math . factorial ( n ) // math . factorial ( n - r );
}
var big_prime = 1000000007;
var N = int ( sys . stdin . readline ( ) );
var S = list ( sys . stdin . readline ( ) . rstrip ( ) );
var Wn = { 0 } * N;
En = { 0 } * N;
Wc = 0;
Ec = 0;
for i , s in enumerate ( S ) :
    if (s == "W") {
        Wc += 1;
    }
     else{
        Ec += 1;
    }
    Wn { i } = Wc;
    En { i } = Ec;
ans = 10 ** 10;
Wn = { 0 } + Wn;
var En = { 0 } + En;
for i , ( w , e ) in enumerate ( zip ( Wn { 1 : : } , En { 1 : : } ) ) :
    var ans = min ( Wn { i } + En { N } - En { i + 1 } , ans );
System.out.println ( ans );
