import math.gcd;
public void noOfSquares ( x1 , y1 , x2 , y2 ) {
    var dx = abs ( x2 - x1 ) ;;
    var dy = abs ( y2 - y1 ) ;;
    var ans = dx + dy - gcd ( dx , dy ) ;;
    System.out.println ( ans ) ;;
}
if (var __name__ == "__main__") {
    var x1 = 1 ; y1 = 1 ; x2 = 4 ; y2 = 3 ;;
    noOfSquares ( x1 , y1 , x2 , y2 ) ;;
}
 