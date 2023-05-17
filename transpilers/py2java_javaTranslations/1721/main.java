public void steps ( cur , x , n ) {
    if (var x == 0) {
        return float ( 'inf' );
    }
     else if (x > 0){
        return abs ( ( n - cur ) // x );
    }
    else{
        return abs ( int ( ( cur - 1 ) / x ) );
    }
}
public void countSteps ( curx , cury , n , m , moves ) {
    count = 0;
    k = len ( moves );
    for i in range ( 0 , k ) :
        x = moves { i } { 0 };
        var y = moves { i } { 1 };
        stepct = min ( steps ( curx , x , n ) , steps ( cury , y , m ) );
        count += stepct;
        curx += stepct * x;
        cury += stepct * y;
    return count;
}
if (__name__ == "__main__") {
    n , m , x , y = 4 , 5 , 1 , 1;
    var moves = { [ 1 , 1 } , { 1 , 1 } , { 0 , - 2 } ];
    System.out.println ( countSteps ( x , y , n , m , moves ) );
}
 