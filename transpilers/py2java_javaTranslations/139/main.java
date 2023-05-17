public void countNonIncreasing ( arr , n ) {
    var cnt = 0 ;;
    var len = 1 ;;
    for i in range ( 0 , n - 1 ) :
        if (( arr { i + 1 } >= arr { i } )) {
            len += 1 ;;
        }
         else{
            cnt += ( ( ( len + 1 ) * len ) / 2 ) ;;
            len = 1 ;;
        }
    if (( len > 1 )) {
        cnt += ( ( ( len - 1 ) * len ) / 2 ) ;;
    }
     return int ( cnt ) ;;
}
if (var __name__ == '__main__') {
    var arr = { 5 , 2 , 3 , 7 , 1 , 1 } ;;
    var n = len ( arr ) ;;
    System.out.println ( countNonIncreasing ( arr , n ) ) ;;
}
 