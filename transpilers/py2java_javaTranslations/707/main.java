import math.log , trunc;
public void checkPowerof8 ( n ) {
    var i = log ( n , 8 );
    return ( i - trunc ( i ) < 0.000001 ) ;;
}
var n = 65;
if (checkPowerof8 ( n )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
