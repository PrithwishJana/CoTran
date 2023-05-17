import math;
public void System.out.printlnSubstrings ( n ) {
    var s = int ( math . log10 ( n ) ) ;;
    var d = ( math . pow ( 10 , s ) ) ;;
    k = d ;;
    while (( n > 0 )) {
        while (( d > 0 )) {
            System.out.println ( int ( n // d ) ) ;;
            d = int ( d / 10 ) ;;
        }
         n = int ( n % k ) ;;
        k = int ( k // 10 ) ;;
        d = k ;;
    }
 }
if (var __name__ == '__main__') {
    var n = 123 ;;
    System.out.printlnSubstrings ( n ) ;;
}
 