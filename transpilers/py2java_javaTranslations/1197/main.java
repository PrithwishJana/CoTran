public void calcFunction ( n , r ) {
    var finalDenominator = 1;
    mx = max ( r , n - r );
    for i in range ( mx + 1 , n + 1 ) :
        denominator = pow ( i , i );
        numerator = pow ( i - mx , i - mx );
        finalDenominator = ( finalDenominator * denominator ) // numerator;
    return finalDenominator;
}
if (var __name__ == "__main__") {
    var n = 6;
    var r = 2;
    System.out.println ( "1/" , var end = "" );
    System.out.println ( calcFunction ( n , r ) );
}
 