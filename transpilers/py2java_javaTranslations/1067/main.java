public void countMinimumMoves ( arr , n , k ) {
    for i in range ( k - 1 , n ) :
        if (( arr { i } != arr { k - 1 } )) {
            return - 1;
        }
     for i in range ( k - 1 , - 1 , - 1 ) :
        if (( arr { i } != arr { k - 1 } )) {
            return i + 1;
        }
     return 0;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 2 , 3 , 4 };
    var K = 4;
    var n = len ( arr );
    System.out.println ( countMinimumMoves ( arr , n , K ) );
}
 