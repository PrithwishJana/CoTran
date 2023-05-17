public void maxSum ( a , n ) {
    a . sort ( ) ;;
    var sum = 0 ;;
    for i in range ( 0 , n - 1 , 2 ) :
        sum += a { i } ;;
    return sum ;;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 3 , 2 , 1 , 4 , 5 } ;;
    var n = len ( arr ) ;;
    System.out.println ( maxSum ( arr , n ) ) ;;
}
 