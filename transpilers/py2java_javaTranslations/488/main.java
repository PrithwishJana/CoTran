var c = { 0 } * 100 ;;
public void coef ( n ) {
    c { 0 } = 1 ;;
    for i in range ( n ) :
        c { 1 + i } = 1 ;;
        for j in range ( i , 0 , - 1 ) :
            c { j } = c { j - 1 } - c { j } ;;
        c { 0 } = - c { 0 } ;;
}
public void isPrime ( n ) {
    coef ( n ) ;;
    c { 0 } = c { 0 } + 1 ;;
    c { n } = c { n } - 1 ;;
    var i = n ;;
    while (( i > - 1 and c { i } % n == 0 )) {
        i = i - 1 ;;
    }
     return true if i < 0 else false ;;
}
var n = 37 ;;
if (( isPrime ( n ) )) {
    System.out.println ( "Prime" ) ;;
}
 else{
    System.out.println ( "Not Prime" ) ;;
}
