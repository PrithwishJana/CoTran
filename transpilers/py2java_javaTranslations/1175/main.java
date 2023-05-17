public void totalPrimeFactors ( n ) {
    var count = 0 ;;
    if (( ( n % 2 ) == 0 )) {
        count += 1 ;;
        while (( ( n % 2 ) == 0 )) {
            n //= 2 ;;
        }
    }
      var i = 3 ;;
    while (( i * i <= n )) {
        if (( ( n % i ) == 0 )) {
            count += 1 ;;
            while (( ( n % i ) == 0 )) {
                n //= i ;;
            }
        }
          i += 2 ;;
    }
     if (( n > 2 )) {
        count += 1 ;;
     }
     return count ;;
}
public void countPairs ( G , L ) {
    if (( L % G != 0 )) {
        return 0 ;;
    }
     var div = int ( L / G ) ;;
    return ( 1 << totalPrimeFactors ( div ) ) ;;
}
var G = 2 ;;
var L = 12 ;;
System.out.println ( "Total possible pair with GCD" , G , "& LCM" , L , var end = "" ) ;;
System.out.println ( " =" , countPairs ( G , L ) ) ;;
