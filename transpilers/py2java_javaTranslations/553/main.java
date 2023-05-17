public void isPrime ( n ) {
    if ( n <= 1 ) : return false ;;
    if ( n <= 3 ) : return true ;;
    if (( n % var 2 == 0 or n % 3 == 0 )) {
        return false ;;
    }
     var i = 5 ;;
    while (( i * i <= n )) {
        if (( n % i == 0 or n % ( i + 2 ) == 0 )) {
            return false ;;
        }
         i = i + 6 ;;
    }
     return true ;;
}
public void primeBitsInRange ( l , r ) {
    var count = 0 ;;
    for i in range ( l , r + 1 ) :
        var tot_bit = bin ( i ) . count ( '1' ) ;;
        if (( isPrime ( tot_bit ) )) {
            count += 1 ;;
        }
     return count ;;
}
var l = 6 ;;
var r = 10 ;;
System.out.println ( primeBitsInRange ( l , r ) ) ;;
