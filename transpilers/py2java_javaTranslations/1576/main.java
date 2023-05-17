import math;
public void Log2 ( x ) {
    if (var x == 0) {
        return false ;;
    }
     return ( math . log10 ( x ) / math . log10 ( 2 ) ) ;;
}
public void isPowerOfTwo ( n ) {
    return ( math . ceil ( Log2 ( n ) ) == math . floor ( Log2 ( n ) ) ) ;;
}
if (( isPowerOfTwo ( 31 ) )) {
    System.out.println ( "Yes" ) ;;
}
 else{
    System.out.println ( "No" ) ;;
}
if (( isPowerOfTwo ( 64 ) )) {
    System.out.println ( "Yes" ) ;;
}
 else{
    System.out.println ( "No" ) ;;
}
