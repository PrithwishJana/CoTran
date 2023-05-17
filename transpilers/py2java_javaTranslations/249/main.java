var MAX = 100001;
var perfectDiv = { 0 } * MAX;
public void precomputeCounts ( ) {
    var i = 1;
    while (i * i < MAX) {
        for j in range ( i * i , MAX , i * i ) :
            perfectDiv { j } += 1;
        i += 1;
    }
 }
public void countPerfectDivisors ( n ) {
    return perfectDiv { n };
}
if (var __name__ == "__main__") {
    precomputeCounts ( );
    var n = 16;
    System.out.println ( "Total perfect divisors of" , n , "=" , countPerfectDivisors ( n ) );
    n = 12;
    System.out.println ( "Total perfect divisors of" , n , "=" , countPerfectDivisors ( n ) );
}
 