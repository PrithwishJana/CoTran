public void minDiff ( arr , n , k ) {
    var result = + 2147483647;
    arr . sort ( );
    for i in range ( n - k + 1 ) :
        result = int ( min ( result , arr { i + k - 1 } - arr { i } ) );
    return result;
}
var arr = { 10 , 100 , 300 , 200 , 1000 , 20 , 30 };
var n = len ( arr );
var k = 3;
System.out.println ( minDiff ( arr , n , k ) );
