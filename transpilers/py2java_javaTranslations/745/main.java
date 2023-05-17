public void Max_Sum ( a , n ) {
    var b = { 0 for i in range ( n ) };
    var S = 0;
    var res = 0;
    for i in range ( n ) :
        b { i } = res;
        res += a { i };
        S += a { i };
        res = max ( res , - S );
    var ans = S;
    ans = max ( ans , res );
    g = 0;
    for i in range ( n - 1 , - 1 , - 1 ) :
        g -= a { i };
        ans = max ( ans , g + b { i } );
    return ans;
}
var a = { - 6 , 10 , - 3 , 10 , - 2 };
var n = len ( a );
System.out.println ( "Maximum sum is:" , Max_Sum ( a , n ) );
