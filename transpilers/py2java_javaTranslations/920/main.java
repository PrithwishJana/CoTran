var MAX = 10;
public void lcs ( dp , arr1 , n , arr2 , m , k ) {
    if (k < 0) {
        return - ( 10 ** 7 );
    }
     if (n < 0 or m < 0) {
        return 0;
    }
     var ans = dp { n } { m } { k };
    if (ans != - 1) {
        return ans;
    }
     ans = max ( lcs ( dp , arr1 , n - 1 , arr2 , m , k ) , lcs ( dp , arr1 , n , arr2 , m - 1 , k ) );
    if (arr1 { n - 1 } == arr2 { m - 1 }) {
        ans = max ( ans , 1 + lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k ) );
    }
     ans = max ( ans , lcs ( dp , arr1 , n - 1 , arr2 , m - 1 , k - 1 ) );
    return ans;
}
if (var __name__ == "__main__") {
    var k = 1;
    var arr1 = { 1 , 2 , 3 , 4 , 5 };
    var arr2 = { 5 , 3 , 1 , 4 , 2 };
    var n = len ( arr1 );
    var m = len ( arr2 );
    var dp = { [ [ - 1 for i in range ( MAX ) } for j in range ( MAX ) ] for k in range ( MAX ) ];
    System.out.println ( lcs ( dp , arr1 , n , arr2 , m , k ) );
}
 