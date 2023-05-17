var max = 4;
public void countWays ( index , cnt , dp , n , m , k ) {
    if (( var index == n )) {
        if (( var cnt == k )) {
            return 1;
        }
         else{
            return 0;
        }
    }
     if (( dp { index } { cnt } != - 1 )) {
        return dp { index } { cnt };
    }
     var ans = 0;
    ans += countWays ( index + 1 , cnt , dp , n , m , k );
    ans += ( m - 1 ) * countWays ( index + 1 , cnt + 1 , dp , n , m , k );
    dp { index } { cnt } = ans;
    return dp { index } { cnt };
}
if (var __name__ == "__main__") {
    var n = 3;
    var m = 3;
    var k = 2;
    var dp = { [ - 1 for x in range ( n + 1 ) } for y in range ( max ) ];
    System.out.println ( m * countWays ( 1 , 0 , dp , n , m , k ) );
}
 