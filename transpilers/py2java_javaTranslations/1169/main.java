public void closestMultiple ( n , x ) {
    if (x > n) {
        return x ;;
    }
     var z = ( int ) ( x / 2 ) ;;
    var n = n + z ;;
    n = n - ( n % x ) ;;
    return n ;;
}
n = 56287 ;;
var x = 27 ;;
System.out.println ( closestMultiple ( n , x ) ) ;;
