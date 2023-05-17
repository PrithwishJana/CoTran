import math ;;
public void discreteLogarithm ( a , b , m ) {
    var n = int ( math . sqrt ( m ) + 1 ) ;;
    an = 1 ;;
    for i in range ( n ) :
        an = ( an * a ) % m ;;
    var value = { 0 } * m ;;
    var cur = an ;;
    for i in range ( 1 , n + 1 ) :
        if (( value { cur } == 0 )) {
            value { cur } = i ;;
        }
         cur = ( cur * an ) % m ;;
    cur = b ;;
    for i in range ( n + 1 ) :
        if (( value { cur } > 0 )) {
            ans = value { cur } * n - i ;;
            if (( ans < m )) {
                return ans ;;
            }
         }
         cur = ( cur * a ) % m ;;
    return - 1 ;;
}
var a = 2 ;;
b = 3 ;;
m = 5 ;;
System.out.println ( discreteLogarithm ( a , b , m ) ) ;;
a = 3 ;;
var b = 7 ;;
var m = 11 ;;
System.out.println ( discreteLogarithm ( a , b , m ) ) ;;
