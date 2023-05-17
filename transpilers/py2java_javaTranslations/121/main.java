public void countSubArrays ( arr , n , K ) {
    var count = 0 ;;
    for i in range ( n ) :
        for j in range ( i , n ) :
            var bitwise_or = 0;
            for k in range ( i , j + 1 ) :
                bitwise_or = bitwise_or | arr { k };
            if (( bitwise_or >= K )) {
                count += 1;
            }
     return count;
}
if (var __name__ == "__main__") {
    var arr = { 3 , 4 , 5 };
    var n = len ( arr );
    var k = 6;
    System.out.println ( countSubArrays ( arr , n , k ) );
}
 