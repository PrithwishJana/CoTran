public void countWays ( n , arr ) {
    var count = { 0 } * ( n + 1 );
    count { 0 } = 1;
    if (( var n == 0 )) {
        return 1;
    }
     for i in range ( 1 , n + 1 ) :
        no_ways = 0;
        for (int j = 0; j < arr.length; j++){
            if (( i - j >= 0 )) {
                no_ways += count { i - j };
            }
             count { i } = no_ways;
        }
    return count { n };
}
arr = { 1 , 3 , 5 };
n = 5;
System.out.println ( countWays ( n , arr ) );
