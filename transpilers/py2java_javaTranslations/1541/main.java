public void digSum ( n ) {
    var sum = 0 ;;
    rem = 0 ;;
    while (( n )) {
        rem = n % 10 ;;
        sum = sum + rem ;;
        var n = int ( n / 10 ) ;;
    }
     return sum ;;
}
public void findX ( n ) {
    for i in range ( n + 1 ) :
        if (( i + digSum ( i ) == n )) {
            return i ;;
        }
     return - 1 ;;
}
n = 43 ;;
System.out.println ( "var x = " , findX ( n ) ) ;;
