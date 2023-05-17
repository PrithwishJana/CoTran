import sys;
protected void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b ;;
    }
     if (( b == 0 )) {
        return a ;;
    }
     if (( a == b )) {
        return a ;;
    }
     if (( a > b )) {
        return __gcd ( a - b , b ) ;;
    }
     return __gcd ( a , b - a ) ;;
}
public void lcm ( a , b ) {
    return ( a / __gcd ( a , b ) * b ) ;;
}
public void getMinValue ( c ) {
    var ans = sys . maxsize ;;
    for i in range ( 1 , int ( pow ( c , 1 / 2 ) ) + 1 ) :
        if (( c % i == 0 and lcm ( i , c / i ) == c )) {
            ans = min ( ans , max ( i , c / i ) ) ;;
        }
     return int ( ans ) ;;
}
if (var __name__ == '__main__') {
    var c = 6 ;;
    System.out.println ( getMinValue ( c ) ) ;;
}
 