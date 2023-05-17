import math.* ;;
public void maxResult ( n , a , b , c ) {
    var maxVal = 0 ;;
    for i in range ( 0 , n + 1 , a ) :
        for j in range ( 0 , n - i + 1 , b ) :
            z = ( n - ( i + j ) ) / c ;;
            if (( floor ( z ) == ceil ( z ) )) {
                x = i // a ;;
                y = j // b ;;
                maxVal = max ( maxVal , x + y + int ( z ) ) ;;
            }
     return maxVal ;;
}
if (var __name__ == "__main__") {
    var n = 10;
    var a = 5;
    var b = 3;
    var c = 4;
    System.out.println ( maxResult ( n , a , b , c ) ) ;;
}
 