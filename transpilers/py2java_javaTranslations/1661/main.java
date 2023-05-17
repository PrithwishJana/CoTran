import sys;
var INT_MAX = sys . maxsize ;;
var INT_MIN = - ( sys . maxsize - 1 );
public void minimumAdjacentDifference ( a , n , k ) {
    var minDiff = INT_MAX ;;
    for i in range ( 1 << n ) :
        cnt = bin ( i ) . count ( '1' ) ;;
        if (( cnt == n - k )) {
            temp = {} ;;
            for j in range ( n ) :
                if (( ( i & ( 1 << j ) ) != 0 )) {
                    temp . append ( a { j } ) ;;
                }
             maxDiff = INT_MIN ;;
            for j in range ( len ( temp ) - 1 ) :
                maxDiff = max ( maxDiff , temp { j + 1 } - temp { j } ) ;;
            minDiff = min ( minDiff , maxDiff ) ;;
        }
     return minDiff ;;
}
if (var __name__ == "__main__") {
    var n = 5 ;;
    var k = 2 ;;
    var a = { 3 , 7 , 8 , 10 , 14 } ;;
    System.out.println ( minimumAdjacentDifference ( a , n , k ) ) ;;
}
 