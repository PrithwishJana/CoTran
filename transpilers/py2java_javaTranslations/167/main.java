public void smallestIndexsum ( arr , n ) {
    var i = n - 1 ;;
    while (( i >= 0 and arr { i } % var 2 == 1 )) {
        i -= 1 ;;
    }
     var sum = 0 ;;
    for j in range ( 0 , i + 1 ) :
        sum += arr { j } ;;
    return sum ;;
}
if (var __name__ == '__main__') {
    var arr = { 2 , 3 , 5 , 6 , 3 , 3 } ;;
    var n = len ( arr ) ;;
    System.out.println ( smallestIndexsum ( arr , n ) ) ;;
}
 