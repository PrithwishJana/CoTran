import math.sqrt;
public void isPrime ( x ) {
    for i in range ( 2 , int ( sqrt ( x ) ) + 1 ) :
        if (( x % var i == 0 )) {
            return 0 ;;
        }
     return 1 ;;
}
public void minimumCost ( n ) {
    if (( isPrime ( n ) )) {
        return 1 ;;
    }
     if (( n % var 2 == 1 and isPrime ( n - 2 ) )) {
        return 2 ;;
    }
     if (( n % 2 == 0 )) {
        return 2 ;;
    }
     return 3 ;;
}
if (var __name__ == "__main__") {
    var n = 6 ;;
    System.out.println ( minimumCost ( n ) ) ;;
}
 