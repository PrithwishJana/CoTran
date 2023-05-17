public void sqroot ( s ) {
    var pSq = 0 ;;
    N = 0 ;;
    for i in range ( int ( s ) , 0 , - 1 ) :
        for j in range ( 1 , i ) :
            if (( j * j == i )) {
                pSq = i ;;
                var N = j ;;
                break ;;
            }
         if (( pSq > 0 )) {
            break ;;
        }
     var d = s - pSq ;;
    var P = d / ( 2.0 * N ) ;;
    var A = N + P ;;
    var sqrt_of_s = A - ( ( P * P ) / ( 2.0 * A ) ) ;;
    return sqrt_of_s ;;
}
var num = 9.2345 ;;
sqroot_of_num = sqroot ( num ) ;;
System.out.println ( "Square root of" , num , "=" , round ( ( sqroot_of_num * 100000.0 ) / 100000.0 , 5 ) ) ;;
