protected void gcd ( a , b ) {
    if (( var a == 0 or b == 0 )) {
        return 0 ;;
    }
     if (( a == b )) {
        return a ;;
    }
     if (( a > b )) {
        return __gcd ( a - b , b ) ;;
    }
     return __gcd ( a , b - a ) ;;
}
public void NumberOfSquares ( x , y ) {
    var s = __gcd ( x , y ) ;;
    ans = ( x * y ) / ( s * s ) ;;
    return int ( ans ) ;;
}
var m = 385 ;;
var n = 60 ;;
System.out.println ( NumberOfSquares ( m , n ) ) ;;
