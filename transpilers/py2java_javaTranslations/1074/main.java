import math;
public void firstDigit ( n ) {
    var digits = ( int ) ( math . log10 ( n ) );
    var n = ( int ) ( n / pow ( 10 , digits ) );
    return n ;;
}
public void lastDigit ( n ) {
    return ( n % 10 );
}
n = 98562 ;;
System.out.println ( firstDigit ( n ) , var end = " " );
System.out.println ( lastDigit ( n ) );
