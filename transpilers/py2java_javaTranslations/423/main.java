public void isSubArray ( A , B , n , m ) {
    var i = 0 ; j = 0 ;;
    while (( i < n and j < m )) {
        if (( A { i } == B { j } )) {
            i += 1 ;;
            j += 1 ;;
            if (( j == m )) {
                return true ;;
            }
         }
         else{
            i = i - j + 1 ;;
            var j = 0 ;;
        }
    }
     return false ;;
}
if (var __name__ == '__main__') {
    var A = { 2 , 3 , 0 , 5 , 1 , 1 , 2 } ;;
    var n = len ( A ) ;;
    var B = { 3 , 0 , 5 , 1 } ;;
    var m = len ( B ) ;;
    if (( isSubArray ( A , B , n , m ) )) {
        System.out.println ( "YES" ) ;;
    }
     else{
        System.out.println ( "NO" ) ;;
    }
}
 