import math.log2;
public void subsetXOR ( arr , n , K ) {
    var max_ele = arr { 0 };
    for i in range ( 1 , n ) :
        if (( arr { i } > max_ele )) {
            max_ele = arr { i };
        }
     var m = ( 1 << int ( log2 ( max_ele ) + 1 ) ) - 1;
    var dp = { [ [ 0 for i in range ( n + 1 ) } for j in range ( m + 1 ) ] for k in range ( n + 1 ) ];
    for i in range ( n + 1 ) :
        for j in range ( m + 1 ) :
            for k in range ( n + 1 ) :
                dp { i } { j } { k } = 0;
    for i in range ( n + 1 ) :
        dp { i } { 0 } { 0 } = 1;
    for i in range ( 1 , n + 1 ) :
        for j in range ( m + 1 ) :
            for k in range ( n + 1 ) :
                dp { i } { j } { k } = dp { i - 1 } { j } { k };
                if (( k != 0 )) {
                    dp { i } { j } { k } += k * dp { i - 1 } { j ^ arr [ i - 1 } ] { k - 1 };
                }
     var ans = 0;
    for i in range ( 1 , n + 1 ) :
        ans += dp { n } { K } { i };
    return ans;
}
if (var __name__ == '__main__') {
    var arr = { 1 , 2 , 3 };
    var k = 1;
    var n = len ( arr );
    System.out.println ( subsetXOR ( arr , n , k ) );
}
 