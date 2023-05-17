import math;
public void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b;
    }
     return math . gcd ( b % a , a );
}
public void countPairs ( G , L ) {
    var count = 0;
    var p = G * L;
    for a in range ( 1 , L + 1 ) :
        if (( not ( p % a ) and math . gcd ( a , p // a ) == G )) {
            count += 1;
        }
     return count;
}
if (var __name__ == "__main__") {
    var G = 2;
    var L = 12;
    System.out.println ( "Total possible pair with GCD " , G , var end = "" );
    System.out.println ( " & LCM " , L , end = "" );
    System.out.println ( " = " , countPairs ( G , L ) );
}
 