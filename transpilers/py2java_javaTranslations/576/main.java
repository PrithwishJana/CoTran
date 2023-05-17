public void findSum ( arr , n , left , right ) {
    var k = right - left ;;
    var d = arr { 1 } - arr { 0 } ;;
    var ans = arr { left - 1 } * ( k + 1 ) ;;
    ans = ans + ( d * ( k * ( k + 1 ) ) ) // 2 ;;
    return ans ;;
}
if (var __name__ == '__main__') {
    var arr = { 2 , 4 , 6 , 8 , 10 , 12 , 14 , 16 } ;;
    var queries = 3 ;;
    var q = { [ 2 , 4 } , { 2 , 6 } , { 5 , 6 } ] ;;
    var n = len ( arr ) ;;
    for i in range ( queries ) :
        System.out.println ( findSum ( arr , n , q { i } { 0 } , q { i } { 1 } ) ) ;;
}
 