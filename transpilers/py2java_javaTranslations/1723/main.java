import math.gcd;
public void cntSubArr ( arr , n ) {
    var ans = 0 ;;
    for i in range ( n ) :
        var curr_gcd = 0 ;;
        for j in range ( i , n ) :
            curr_gcd = gcd ( curr_gcd , arr { j } ) ;;
            ans += ( curr_gcd == 1 ) ;;
    return ans ;;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 1 , 1 } ;;
    var n = len ( arr ) ;;
    System.out.println ( cntSubArr ( arr , n ) ) ;;
}
 