import sys;
public void FindMinimumCost ( ind , a , n , k , dp ) {
    if (( var ind == ( n - 1 ) )) {
        return 0;
    }
     else if (( dp { ind } != - 1 )){
        return dp { ind };
    }
    else{
        var ans = sys . maxsize;
        for i in range ( 1 , k + 1 ) :
            if (( ind + i < n )) {
                ans = min ( ans , abs ( a { ind + i } - a { ind } ) + FindMinimumCost ( ind + i , a , n , k , dp ) );
            }
             else{
                break;
            }
        dp { ind } = ans;
        return ans;
    }
}
if (var __name__ == '__main__') {
    var a = { 10 , 30 , 40 , 50 , 20 };
    var k = 3;
    var n = len ( a );
    var dp = { - 1 for i in range ( n ) };
    System.out.println ( FindMinimumCost ( 0 , a , n , k , dp ) );
}
 