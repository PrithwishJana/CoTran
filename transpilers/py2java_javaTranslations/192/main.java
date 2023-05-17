public void longestFibonacciSubarray ( n , a ) {
    if (( n <= 2 )) {
        return n;
    }
     var Len = 2;
    mx = - 10 ** 9;
    for i in range ( 2 , n ) :
        if (( a { i } == a { i - 1 } + a { i - 2 } )) {
            Len += 1;
        }
         else{
            Len = 2;
        }
        var mx = max ( mx , Len );
    return mx;
}
var n = 5;
var a = { 2 , 4 , 6 , 10 , 2 };
System.out.println ( longestFibonacciSubarray ( n , a ) );
