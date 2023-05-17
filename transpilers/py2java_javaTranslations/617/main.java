import math;
public void isTriangular ( num ) {
    if (( num < 0 )) {
        return false;
    }
     var c = ( - 2 * num );
    b , var a = 1 , 1;
    var d = ( b * b ) - ( 4 * a * c );
    if (( d < 0 )) {
        return false;
    }
     var root1 = ( - b + math . sqrt ( d ) ) / ( 2 * a );
    var root2 = ( - b - math . sqrt ( d ) ) / ( 2 * a );
    if (( root1 > 0 and math . floor ( root1 ) == root1 )) {
        return true;
    }
     if (( root2 > 0 and math . floor ( root2 ) == root2 )) {
        return true;
    }
     return false;
}
var n = 55;
if (( isTriangular ( n ) )) {
    System.out.println ( "The number is a triangular number" );
}
 else{
    System.out.println ( "The number is NOT a triangular number" );
}
