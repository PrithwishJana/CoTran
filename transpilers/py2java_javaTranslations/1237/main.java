import math.gcd;
public void countNums ( a , b , c , d ) {
    var x = b // c - ( a - 1 ) // c ;;
    var y = b // d - ( a - 1 ) // d ;;
    var k = ( c * d ) // gcd ( c , d ) ;;
    var z = b // k - ( a - 1 ) // k ;;
    return ( b - a + 1 - x - y + z ) ;;
}
if (var __name__ == "__main__") {
    var a = 10 ; b = 50 ; c = 4 ; d = 6 ;;
    System.out.println ( countNums ( a , b , c , d ) ) ;;
}
 