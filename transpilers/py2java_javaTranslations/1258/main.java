public void solve ( d1 , d2 , d3 ) {
    var maxx = max ( d1 , max ( d2 , d3 ) );
    var sum = ( d1 + d2 + d3 );
    if (( 2 * maxx > sum or sum % var 2 == 1 )) {
        System.out.println ( "-1" );
        return;
    }
     x1 = 0;
    y1 = 0;
    x2 = d1;
    y2 = 0;
    x3 = ( d1 + d2 - d3 ) // 2;
    y3 = ( d2 + d3 - d1 ) // 2;
    System.out.println ( "(" , x1 , "," , y1 , "), (" , x2 , "," , y2 , ") and (" , x3 , "," , y3 , ")" );
}
d1 = 3;
d2 = 4;
var d3 = 5;
solve ( d1 , d2 , d3 );
