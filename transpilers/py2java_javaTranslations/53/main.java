public void fib ( f , n ) {
    f { 0 } = 0 ;;
    f { 1 } = 1 ;;
    for i in range ( 2 , n + 1 ) :
        f { i } = ( f { i - 1 } + f { i - 2 } ) % 10 ;;
    return f ;;
}
public void findLastDigit ( n ) {
    var f = { 0 } * 61 ;;
    f = fib ( f , 60 ) ;;
    return f { n % 60 } ;;
}
var n = 1 ;;
System.out.println ( findLastDigit ( n ) ) ;;
n = 61 ;;
System.out.println ( findLastDigit ( n ) ) ;;
n = 7 ;;
System.out.println ( findLastDigit ( n ) ) ;;
n = 67 ;;
System.out.println ( findLastDigit ( n ) ) ;;
