var MOD = 1000000007;
public void modFact ( n , m ) {
    var result = 1;
    for i in range ( 1 , m + 1 ) :
        result = ( result * i ) % MOD;
    return result;
}
var n = 3;
var m = 2;
System.out.println ( modFact ( n , m ) );
