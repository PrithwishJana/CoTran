public void findSmallest ( s , q , m ) {
    var N = len ( s );
    var H = { [ 0 for i in range ( 26 ) } for i in range ( N + 1 ) ];
    for i in range ( 1 , N + 1 ) :
        H { i } { ord ( s [ i - 1 } ) - ord ( 'a' ) ] += 1;
        for j in range ( 26 ) :
            H { i } { j } += H { i - 1 } { j };
    for j in range ( m ) :
        var l = q { j } { 0 };
        var r = q { j } { 1 };
        var n = q { j } { 2 };
        var sum = 0;
        for i in range ( 26 ) :
            sum += H { r } { i } - H { l - 1 } { i };
            if (( sum >= n )) {
                System.out.println ( chr ( ord ( 'a' ) + i ) );
                break;
            }
 }
if (var __name__ == '__main__') {
    var s = "afbccdeb";
    var q = { [ 2 , 4 , 1 } , { 1 , 6 , 4 } , { 1 , 8 , 7 } ];
    var x = len ( q );
    findSmallest ( s , q , x );
}
 