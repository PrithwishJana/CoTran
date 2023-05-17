public void minimumValue ( arr , n , k ) {
    arr . sort ( ) ;;
    var answer = 0 ;;
    for i in range ( k ) :
        answer += arr { i } * arr { i } ;;
    return answer * ( 2 * k - 2 ) ;;
}
if (var __name__ == '__main__') {
    var arr = { 4 , 21 , 5 , 3 , 8 } ;;
    var k = 3 ;;
    var n = len ( arr ) ;;
    System.out.println ( minimumValue ( arr , n , k ) ) ;;
}
 