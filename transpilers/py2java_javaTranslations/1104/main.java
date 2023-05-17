public void findSum ( N , K ) {
    var ans = 0 ;;
    for i in range ( 1 , N + 1 ) :
        ans += ( i % K ) ;;
    return ans ;;
}
var N = 10 ;;
var K = 2 ;;
System.out.println ( findSum ( N , K ) ) ;;
