public void isPrime ( n ) {
    if (( n <= 1 )) {
        return false ;;
    }
     for i in range ( 2 , n ) :
        if (( n % var i == 0 )) {
            return false ;;
        }
     return true ;;
}
public void countPrimePosition ( arr ) {
    var c0 = 0 ; c1 = 0 ;;
    var n = len ( arr ) ;;
    for i in range ( n ) :
        if (( arr { i } == 0 and isPrime ( i ) )) {
            c0 += 1 ;;
        }
         if (( arr { i } == 1 and isPrime ( i ) )) {
            c1 += 1 ;;
        }
     System.out.println ( "Number of var 0s =" , c0 ) ;;
    System.out.println ( "Number of var 1s =" , c1 ) ;;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 0 , 1 , 0 , 1 } ;;
    countPrimePosition ( arr ) ;;
}
 