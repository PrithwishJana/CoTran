import math.gcd as __gcd;
var MAX = 100;
public void recur ( ind , cnt , last , a , n , k , dp ) {
    if (( var cnt == k )) {
        return 0;
    }
     if (( var ind == n )) {
        return - 10 ** 9;
    }
     if (( dp { ind } { cnt } != - 1 )) {
        return dp { ind } { cnt };
    }
     var ans = 0;
    for i in range ( ind , n ) :
        if (( cnt % 2 == 0 )) {
            ans = max ( ans , recur ( i + 1 , cnt + 1 , i , a , n , k , dp ) );
        }
         else{
            ans = max ( ans , __gcd ( a { last } , a { i } ) + recur ( i + 1 , cnt + 1 , 0 , a , n , k , dp ) );
        }
    dp { ind } { cnt } = ans;
    return ans;
}
var a = { 4 , 5 , 3 , 7 , 8 , 10 , 9 , 8 };
var n = len ( a );
var k = 4 ;;
var dp = { [ - 1 for i in range ( MAX ) } for i in range ( n ) ];
System.out.println ( recur ( 0 , 0 , 0 , a , n , k , dp ) );
