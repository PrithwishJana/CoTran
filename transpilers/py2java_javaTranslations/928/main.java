import math;
public void fib ( n ) {
    var phi = ( 1 + math . sqrt ( 5 ) ) / 2 ;;
    return int ( round ( pow ( phi , n ) / math . sqrt ( 5 ) ) ) ;;
}
public void calculateSum ( l , r ) {
    var sum = fib ( r + 2 ) - fib ( l + 1 ) ;;
    return sum ;;
}
var l = 4 ;;
var r = 8 ;;
System.out.println ( calculateSum ( l , r ) ) ;;
