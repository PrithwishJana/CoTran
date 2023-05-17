public void flipSign ( a ) {
    var neg = 0 ;;
    var tmp = 1 if a < 0 else - 1 ;;
    while (( a != 0 )) {
        neg += tmp ;;
        a += tmp ;;
    }
     return neg ;;
}
public void areDifferentSign ( a , b ) {
    return ( ( a < 0 and b > 0 ) or ( a > 0 and b < 0 ) ) ;;
}
public void sub ( a , b ) {
    return a + flipSign ( b ) ;;
}
public void mul ( a , b ) {
    if (( a < b )) {
        return mul ( b , a ) ;;
    }
     var sum = 0 ;;
    for i in range ( abs ( b ) , 0 , - 1 ) :
        sum += a ;;
    if (( b < 0 )) {
        sum = flipSign ( sum ) ;;
    }
     return sum ;;
}
public void division ( a , b ) {
    var quotient = 0 ;;
    divisor = flipSign ( abs ( b ) ) ;;
    for dividend in range ( abs ( a ) , abs ( divisor ) + divisor , divisor ) :
        quotient += 1 ;;
    if (( areDifferentSign ( a , b ) )) {
        quotient = flipSign ( quotient ) ;;
    }
     return quotient ;;
}
System.out.println ( "Subtraction is" , sub ( 4 , - 2 ) ) ;;
System.out.println ( "Product is" , mul ( - 9 , 6 ) ) ;;
a , var b = 8 , 2 ;;
if (( b )) {
    System.out.println ( "Division is" , division ( a , b ) ) ;;
}
 else{
    System.out.println ( "Exception :- Divide by 0" ) ;;
}
