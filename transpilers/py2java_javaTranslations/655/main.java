public void maxPrimefactorNum ( N ) {
    if (( N < 2 )) {
        return 0 ;;
    }
     var arr = { true } * ( N + 1 ) ;;
    var prod = 1 ;;
    var res = 0 ;;
    var p = 2 ;;
    while (( p * p <= N )) {
        if (( arr { p } == true )) {
            for i in range ( p * 2 , N + 1 , p ) :
                arr { i } = false ;;
            prod *= p ;;
            if (( prod > N )) {
                return res ;;
            }
             res += 1 ;;
        }
         p += 1 ;;
    }
     return res ;;
}
var N = 500 ;;
System.out.println ( maxPrimefactorNum ( N ) ) ;;
