import math as mt;
public void isPerfectSquare ( x ) {
    var sr = mt . sqrt ( x );
    return ( ( sr - mt . floor ( sr ) ) == 0 );
}
public void isSunnyNum ( n ) {
    if (( isPerfectSquare ( n + 1 ) )) {
        return true;
    }
     return false;
}
var n = 3;
if (( isSunnyNum ( n ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
