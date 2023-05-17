public void countElements ( p , n ) {
    var ans = 0 ;;
    for i in range ( 1 , n - 1 ) :
        if (( p { i - 1 } > p { i } and p { i } > p { i + 1 } )) {
            ans += 1 ;;
        }
         else if (( p { i - 1 } < p { i } and p { i } < p { i + 1 } )){
            ans += 1 ;;
        }
    return ans ;;
}
if (var __name__ == "__main__") {
    var p = { 2 , 5 , 1 , 3 , 4 } ;;
    var n = len ( p ) ;;
    System.out.println ( countElements ( p , n ) ) ;;
}
 