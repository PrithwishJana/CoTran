public void minOperations ( ar , k ) {
    var ar = sorted ( ar );
    var opsNeeded = 0;
    for i in range ( k ) :
        opsNeeded += ar { k - 1 } - ar { i };
    ans = opsNeeded;
    for i in range ( k , len ( ar ) ) :
        opsNeeded = opsNeeded - ( ar { i - 1 } - ar { i - k } );
        opsNeeded += ( k - 1 ) * ( ar { i } - ar { i - 1 } );
        var ans = min ( ans , opsNeeded );
    return ans;
}
var arr = { 3 , 1 , 9 , 100 };
var n = len ( arr );
var k = 3;
System.out.println ( minOperations ( arr , k ) );
