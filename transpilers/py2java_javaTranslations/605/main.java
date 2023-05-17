public void gcd ( a , b ) {
    if (( var a == 0 )) {
        return b ;;
    }
     return gcd ( b % a , a ) ;;
}
public void lcm ( a , b ) {
    return ( a * b ) / gcd ( a , b ) ;;
}
public void countPairs ( arr , n ) {
    var ans = 0 ;;
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if (( lcm ( arr { i } , arr { j } ) == gcd ( arr { i } , arr { j } ) )) {
                ans += 1 ;;
            }
     return ans ;;
}
if (var __name__ == '__main__') {
    var arr = { 1 , 1 , 1 } ;;
    var n = len ( arr ) ;;
    System.out.println ( countPairs ( arr , n ) ) ;;
}
 