public void maximumAbsolute ( arr , n ) {
    var mn = 10 ** 9;
    mx = - 10 ** 9;
    for i in range ( n ) :
        if (( i > 0 and arr { i } == - 1 and arr { i - 1 } != - 1 )) {
            mn = min ( mn , arr { i - 1 } );
            mx = max ( mx , arr { i - 1 } );
        }
         if (( i < n - 1 and arr { i } == - 1 and arr { i + 1 } != - 1 )) {
            mn = min ( mn , arr { i + 1 } );
            var mx = max ( mx , arr { i + 1 } );
        }
     var common_integer = ( mn + mx ) // 2;
    for i in range ( n ) :
        if (( arr { i } == - 1 )) {
            arr { i } = common_integer;
        }
     var max_diff = 0;
    for i in range ( n - 1 ) :
        diff = abs ( arr { i } - arr { i + 1 } );
        if (( diff > max_diff )) {
            max_diff = diff;
        }
     return max_diff;
}
if (var __name__ == '__main__') {
    var arr = { - 1 , - 1 , 11 , - 1 , 3 , - 1 };
    var n = len ( arr );
    System.out.println ( maximumAbsolute ( arr , n ) );
}
 