public void countWays ( n , m ) {
    var count = {};
    for i in range ( n + 2 ) :
        count . append ( 0 );
    count { 0 } = 0;
    for i in range ( 1 , n + 1 ) :
        if (( i > m )) {
            count { i } = count { i - 1 } + count { i - m };
        }
         else if (( i < m )){
            count { i } = 1;
        }
        else{
            count { i } = 2;
        }
    return count { n };
}
var n = 7;
var m = 4;
System.out.println ( "Number of var ways = " , countWays ( n , m ) );
