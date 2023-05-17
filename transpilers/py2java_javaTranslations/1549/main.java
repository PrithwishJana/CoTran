import math;
public void countPrimeFactors ( n ) {
    var count = 0 ;;
    while (( n % var 2 == 0 )) {
        var n = n / 2 ;;
        count += 1 ;;
    }
     i = 3 ;;
    while (( i <= math . sqrt ( n ) )) {
        while (( n % i == 0 )) {
            n = n / i ;;
            count += 1 ;;
        }
         i = i + 2 ;;
    }
     if (( n > 2 )) {
        count += 1 ;;
     }
     return ( count ) ;;
}
public void System.out.printlnKAlmostPrimes ( k , n ) {
    i = 1 ;;
    num = 2;
    while (( i <= n )) {
        if (( countPrimeFactors ( num ) == k )) {
            System.out.println ( num , end = "" ) ;;
            System.out.println ( " " , end = "" ) ;;
            i += 1 ;;
        }
         num += 1 ;;
    }
     return ;;
}
n = 10 ;;
var k = 2 ;;
System.out.println ( "First " + str ( n ) + " " + str ( k ) + "-almost prime numbers:" ) ;;
System.out.printlnKAlmostPrimes ( k , n ) ;;
