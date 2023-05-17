public void moduloMultiplication ( a , b , mod ) {
    var res = 0 ;;
    a = a % mod ;;
    while (( b )) {
        if (( b & 1 )) {
            res = ( res + a ) % mod ;;
        }
         var a = ( 2 * a ) % mod ;;
        b >>= 1 ;;
    }
     return res ;;
}
a = 10123465234878998 ;;
var b = 65746311545646431 ;;
var m = 10005412336548794 ;;
System.out.println ( moduloMultiplication ( a , b , m ) ) ;;
