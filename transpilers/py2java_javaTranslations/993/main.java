public void countWays ( arr , m , N ) {
    var count = { 0 for i in range ( N + 1 ) };
    count { 0 } = 1;
    for i in range ( 1 , N + 1 ) :
        for j in range ( m ) :
            if (( i >= arr { j } )) {
                count { i } += count { i - arr [ j } ];
            }
     return count { N };
}
var arr = { 1 , 5 , 6 };
var m = len ( arr );
var N = 7;
System.out.println ( "Total number of var ways = " , countWays ( arr , m , N ) );
