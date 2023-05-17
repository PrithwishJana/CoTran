public void calculateSum ( n , k ) {
    var res = 1;
    MOD = 1000000007;
    for i in range ( 0 , k ) :
        res = ( res * n ) % MOD;
    return res;
}
var n = 4;
var k = 3;
System.out.println ( calculateSum ( n , k ) );
