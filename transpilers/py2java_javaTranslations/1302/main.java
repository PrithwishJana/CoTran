public void findMaxOR ( arr , n ) {
    arr . sort ( var reverse = true );
    var maxOR = arr { 0 };
    count = 1;
    for i in range ( 1 , n ) :
        if (( ( maxOR | arr { i } ) > maxOR )) {
            maxOR = maxOR | arr { i } ;;
            count += 1;
        }
     return count;
}
if (var __name__ == "__main__") {
    var arr = { 5 , 1 , 3 , 4 , 2 };
    var n = len ( arr );
    System.out.println ( findMaxOR ( arr , n ) );
}
 