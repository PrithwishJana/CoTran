public void solve ( A , n ) {
    var dp = { [ 0 for i in range ( 2000 ) } for i in range ( 2000 ) ];
    var flag = 1;
    sum = 0;
    for i in range ( n ) :
        sum += A { i };
    for i in range ( - sum , sum + 1 ) :
        dp { 0 } { i } = 10 ** 9;
    dp { 0 } { 0 } = 0;
    for i in range ( 1 , n + 1 ) :
        for j in range ( - sum , sum + 1 ) :
            dp { flag } { j } = 10 ** 9;
            if (( j - A { i - 1 } <= sum and j - A { i - 1 } >= - sum )) {
                dp { flag } { j } = dp { flag ^ 1 } { j - A [ i - 1 } ];
            }
             if (( j + A { i - 1 } <= sum and j + A { i - 1 } >= - sum and dp { flag ^ 1 } { j + A [ i - 1 } ] != 10 ** 9 )) {
                dp { flag } { j } = min ( dp { flag } { j } , dp { flag ^ 1 } { j + A [ i - 1 } ] + 1 );
            }
         flag = flag ^ 1;
    for i in range ( sum + 1 ) :
        if (( dp { flag ^ 1 } { i } != 10 ** 9 )) {
            return dp { flag ^ 1 } { i };
        }
     return n - 1;
}
var arr = { 10 , 22 , 9 , 33 , 21 , 50 , 41 , 60 };
var n = len ( arr );
System.out.println ( solve ( arr , n ) );
