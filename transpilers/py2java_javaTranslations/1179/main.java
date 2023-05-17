public void next ( arr , target ) {
    var start = 0 ;;
    end = len ( arr ) - 1 ;;
    ans = - 1 ;;
    while (( start <= end )) {
        mid = ( start + end ) // 2 ;;
        if (( arr { mid } <= target )) {
            start = mid + 1 ;;
        }
         else{
            var ans = mid ;;
            var end = mid - 1 ;;
        }
    }
     return ans ;;
}
if (var __name__ == '__main__') {
    var arr = { 1 , 2 , 3 , 5 , 8 , 12 } ;;
    System.out.println ( next ( arr , 8 ) ) ;;
}
 