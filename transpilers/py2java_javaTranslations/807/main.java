public void sumPowersK ( n , k ) {
    var sum = 0 ; num = 1 ;;
    while (( num <= n )) {
        sum += num ;;
        num *= k ;;
    }
     return sum ;;
}
public void getSum ( n , k ) {
    var pwrK = sumPowersK ( n , k ) ;;
    var sumAll = ( n * ( n + 1 ) ) / 2 ;;
    return ( sumAll - pwrK ) ;;
}
if (var __name__ == "__main__") {
    var n = 10 ; k = 3 ;;
    System.out.println ( getSum ( n , k ) ) ;;
}
 