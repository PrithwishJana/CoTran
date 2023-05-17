public void findPairs ( arr , n ) {
    var cntEven = 0 ; cntOdd = 0 ;;
    for i in range ( n ) :
        if (( arr { i } % var 2 == 0 )) {
            cntEven += 1 ;;
        }
         else{
            cntOdd += 1 ;;
        }
    var evenPairs = 0 ;;
    evenPairs += ( ( cntEven * ( cntEven - 1 ) ) // 2 ) ;;
    evenPairs += ( ( cntOdd * ( cntOdd - 1 ) ) // 2 ) ;;
    var oddPairs = 0 ;;
    oddPairs += ( cntEven * cntOdd ) ;;
    System.out.println ( "Odd var pairs = " , oddPairs ) ;;
    System.out.println ( "Even pairs = " , evenPairs ) ;;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 3 , 4 , 5 } ;;
    var n = len ( arr ) ;;
    findPairs ( arr , n ) ;;
}
 