public void CountSubSet ( arr , n , X ) {
    var N = 2 ** n ;;
    var count = 0 ;;
    for i in range ( N ) :
        for j in range ( n ) :
            if (( i & ( 1 << j ) )) {
                if (( arr { j } == X )) {
                    count += 1 ;;
                }
             }
     return count ;;
}
if (var __name__ == "__main__") {
    var arr = { 4 , 5 , 6 , 7 } ;;
    var X = 5 ;;
    var n = len ( arr ) ;;
    System.out.println ( CountSubSet ( arr , n , X ) ) ;;
}
 