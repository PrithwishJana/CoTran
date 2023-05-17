public void countPairs ( n ) {
    var count = 0 ;;
    for x in range ( 1 , n ) :
        for y in range ( x + 1 , n + 1 ) :
            if (( ( y + x ) % ( y ^ x ) == 0 )) {
                count += 1 ;;
            }
     return count ;;
}
if (var __name__ == "__main__") {
    var n = 6 ;;
    System.out.println ( countPairs ( n ) ) ;;
}
 