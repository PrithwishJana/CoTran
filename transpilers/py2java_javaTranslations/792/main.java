import math;
public void divSum ( n ) {
    var sum = 1 ;;
    i = 2 ;;
    while (( i * i <= n )) {
        if (( n % i == 0 )) {
            sum = ( sum + i + math . floor ( n / i ) ) ;;
        }
         i += 1 ;;
    }
     return sum ;;
}
public void areEquivalent ( num1 , num2 ) {
    return divSum ( num1 ) == divSum ( num2 ) ;;
}
var num1 = 559 ;;
var num2 = 703 ;;
if (( areEquivalent ( num1 , num2 ) == true )) {
    System.out.println ( "Equivalent" ) ;;
}
 else{
    System.out.println ( "Not Equivalent" ) ;;
}
