public void fib ( n ) {
    var phi = ( ( 1 + ( 5 ** ( 1 / 2 ) ) ) / 2 ) ;;
    return round ( ( phi ** n ) / ( 5 ** ( 1 / 2 ) ) ) ;;
}
public void calculateSum ( l , r ) {
    var sum = 0 ;;
    for i in range ( l , r + 1 ) :
        sum += fib ( i ) ;;
    return sum ;;
}
if (var __name__ == '__main__') {
    l , var r = 4 , 8 ;;
    System.out.println ( calculateSum ( l , r ) ) ;;
}
 