public void productDiagonals ( arr , n ) {
    var product = 1 ;;
    for i in range ( n ) :
        product = product * arr { i } { i } ;;
        product = product * arr { i } { n - i - 1 } ;;
    if (( n % 2 == 1 )) {
        product = product // arr { n // 2 } { n // 2 } ;;
    }
     return product ;;
}
if (var __name__ == '__main__') {
    var arr1 = { [ 1 , 2 , 3 , 4 } , { 5 , 6 , 7 , 8 } , { 9 , 7 , 4 , 2 } , { 2 , 2 , 2 , 1 } ] ;;
    System.out.println ( productDiagonals ( arr1 , 4 ) ) ;;
    var arr2 = { [ 2 , 1 , 2 , 1 , 2 } , { 1 , 2 , 1 , 2 , 1 } , { 2 , 1 , 2 , 1 , 2 } , { 1 , 2 , 1 , 2 , 1 } , { 2 , 1 , 2 , 1 , 2 } ] ;;
    System.out.println ( productDiagonals ( arr2 , 5 ) ) ;;
}
 