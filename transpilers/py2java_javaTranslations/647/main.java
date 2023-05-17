import math;
public void cone ( a ) {
    if (( a < 0 )) {
        return - 1 ;;
    }
     var r = ( a * math . sqrt ( 2 ) ) / 3 ;;
    var h = ( 2 * a ) / 3 ;;
    var V = 3.14 * math . pow ( r , 2 ) * h ;;
    return V ;;
}
var a = 5 ;;
System.out.println ( "{:.4f}" . format ( cone ( a ) ) ) ;;
