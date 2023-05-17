public void isDivisible ( n ) {
    var temp = n;
    var sum = 0 ;;
    while (( n )) {
        k = n % 10 ;;
        sum += k ;;
        n /= 10 ;;
    }
     if (( temp % sum == 0 )) {
        return "YES" ;;
     }
     return "NO" ;;
}
var n = 123 ;;
System.out.println ( isDivisible ( n ) ) ;;
