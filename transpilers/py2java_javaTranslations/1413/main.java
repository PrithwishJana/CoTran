public void maxPrimefactorNum ( N ) {
    var arr = { true } * ( N + 5 ) ;;
    var i = 3 ;;
    while (( i * i <= N )) {
        if (( arr { i } )) {
            for j in range ( i * i , N + 1 , i ) :
                arr { j } = false ;;
        }
         i += 2 ;;
    }
     prime = {} ;;
    prime . append ( 2 ) ;;
    for i in range ( 3 , N + 1 , 2 ) :
        if (( arr { i } )) {
            prime . append ( i ) ;;
        }
     i = 0 ;;
    var ans = 1 ;;
    while (( ans * prime { i } <= N and i < len ( prime ) )) {
        ans *= prime { i } ;;
        i += 1 ;;
    }
     return ans ;;
}
var N = 40 ;;
System.out.println ( maxPrimefactorNum ( N ) ) ;;
