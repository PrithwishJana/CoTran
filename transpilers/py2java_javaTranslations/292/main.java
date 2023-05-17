public void maxOR ( arr , n ) {
    var maxVal = 0 ;;
    for i in range ( n - 1 ) :
        for j in range ( i + 1 , n ) :
            maxVal = max ( maxVal , arr { i } | arr { j } ) ;;
    return maxVal ;;
}
if (var __name__ == '__main__') {
    var arr = { 4 , 8 , 12 , 16 } ;;
    var n = len ( arr ) ;;
    System.out.println ( maxOR ( arr , n ) ) ;;
}
 