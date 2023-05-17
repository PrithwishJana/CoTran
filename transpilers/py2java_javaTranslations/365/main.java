public void getMinimumOps ( ar ) {
    var n = len ( ar );
    var small = min ( ar );
    var large = max ( ar );
    var dp = { [ 0 for i in range ( large + 1 ) } for i in range ( n ) ];
    for j in range ( small , large + 1 ) :
        dp { 0 } { j } = abs ( ar { 0 } - j );
    for i in range ( 1 , n ) :
        var minimum = 10 ** 9;
        for j in range ( small , large + 1 ) :
            minimum = min ( minimum , dp { i - 1 } { j } );
            dp { i } { j } = minimum + abs ( ar { i } - j );
    var ans = 10 ** 9;
    for j in range ( small , large + 1 ) :
        ans = min ( ans , dp { n - 1 } { j } );
    return ans;
}
var ar = { 1 , 2 , 1 , 4 , 3 };
System.out.println ( getMinimumOps ( ar ) );
