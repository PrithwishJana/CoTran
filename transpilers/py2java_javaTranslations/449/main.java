import sys;
public void maxProductSum ( string , m ) {
    var n = len ( string );
    maxProd , var maxSum = ( - ( sys . maxsize ) - 1 , - ( sys . maxsize ) - 1 );
    for i in range ( n - m ) :
        product , sum = 1 , 0;
        for j in range ( i , m + i ) :
            product = product * ( ord ( string { j } ) - ord ( '0' ) );
            sum = sum + ( ord ( string { j } ) - ord ( '0' ) );
        maxProd = max ( maxProd , product );
        maxSum = max ( maxSum , sum );
    System.out.println ( "Maximum var Product =" , maxProd );
    System.out.println ( "Maximum var Sum =" , maxSum );
}
if (var __name__ == "__main__") {
    var string = "3675356291";
    var m = 5;
    maxProductSum ( string , m );
}
 