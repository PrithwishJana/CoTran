import math.floor , log2;
public void minAbsDiff ( n ) {
    var left = pow ( 2 , floor ( log2 ( n ) ) );
    var right = left * 2;
    return min ( ( n - left ) , ( right - n ) );
}
if (var __name__ == "__main__") {
    var n = 15;
    System.out.println ( minAbsDiff ( n ) );
}
 