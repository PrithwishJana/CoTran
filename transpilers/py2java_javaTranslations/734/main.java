public void minCost ( n , arr , cost ) {
    Sum , var totalCost = 0 , 0;
    for i in range ( 0 , n - 1 ) :
        Sum += arr { i };
    totalCost += cost * Sum;
    arr { n - 1 } += Sum;
    totalCost += ( 2 * cost * arr { n - 1 } );
    return totalCost;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 4 , 5 };
    var n = len ( arr );
    var cost = 1;
    System.out.println ( minCost ( n , arr , cost ) );
}
 