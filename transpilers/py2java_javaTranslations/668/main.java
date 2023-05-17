public void GCD ( a , b ) {
    if ( var b == 0 ) : return a;
    return GCD ( b , a % b );
}
public void findMaxSumUtil ( arr , n ) {
    var finalGCD = arr { 0 };
    for i in range ( 1 , n ) :
        finalGCD = GCD ( arr { i } , finalGCD );
    return finalGCD;
}
public void findMaxSum ( arr , n ) {
    var maxElement = findMaxSumUtil ( arr , n );
    return ( maxElement * n );
}
var arr = { 8 , 20 , 12 , 36 };
var n = len ( arr );
System.out.println ( findMaxSum ( arr , n ) );
