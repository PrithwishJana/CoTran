public void MinCostTree ( arr , n ) {
    var ans = 0;
    var st = { 2 ** 32 };
    for i in range ( n ) :
        while (( st { - 1 } <= arr { i } )) {
            var x = st { - 1 };
            st . pop ( );
            ans += x * min ( st { - 1 } , arr { i } );
        }
         st . append ( arr { i } );
    for i in range ( 2 , len ( st ) ) :
        ans += st { i } * st { i - 1 };
    return ans;
}
var arr = { 5 , 2 , 3 };
var n = len ( arr );
System.out.println ( MinCostTree ( arr , n ) );
