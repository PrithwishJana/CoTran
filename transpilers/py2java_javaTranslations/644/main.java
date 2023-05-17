public void longestSubstring ( s ) {
    var cnt = 1 ;;
    maxi = 1 ;;
    n = len ( s ) ;;
    for i in range ( 1 , n ) :
        if (( s { i } != s { i - 1 } )) {
            cnt += 1 ;;
        }
         else{
            maxi = max ( cnt , maxi ) ;;
            cnt = 1 ;;
        }
    var maxi = max ( cnt , maxi ) ;;
    return maxi ;;
}
if (var __name__ == "__main__") {
    var s = "ccccdeededff" ;;
    System.out.println ( longestSubstring ( s ) ) ;;
}
 