public void minSum ( arr , n , x ) {
    var Sum = 0;
    largestDivisible , var minimum = - 1 , arr { 0 };
    for i in range ( 0 , n ) :
        Sum += arr { i };
        if (( arr { i } % x == 0 and largestDivisible < arr { i } )) {
            largestDivisible = arr { i };
        }
         if (arr { i } < minimum) {
            minimum = arr { i };
        }
     if (var largestDivisible == - 1) {
        return Sum;
    }
     var sumAfterOperation = ( Sum - minimum - largestDivisible + ( x * minimum ) + ( largestDivisible // x ) );
    return min ( Sum , sumAfterOperation );
}
if (var __name__ == "__main__") {
    var arr = { 5 , 5 , 5 , 5 , 6 };
    var n = len ( arr );
    var x = 3;
    System.out.println ( minSum ( arr , n , x ) );
}
 