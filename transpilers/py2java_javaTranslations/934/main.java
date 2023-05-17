public void sumAP ( n , d ) {
    var n = int ( n / d ) ;;
    return ( n ) * ( 1 + n ) * ( d / 2 ) ;;
}
public void sumMultiples ( n ) {
    n -= 1 ;;
    return ( int ( sumAP ( n , 2 ) + sumAP ( n , 5 ) - sumAP ( n , 10 ) ) ) ;;
}
n = 20 ;;
System.out.println ( sumMultiples ( n ) ) ;;
