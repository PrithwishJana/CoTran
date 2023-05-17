public void countWays ( n ) {
    var counter = 0;
    for i in range ( 1 , n ) :
        for j in range ( i , n ) :
            for k in range ( j , n ) :
                for l in range ( k , n ) :
                    if (( i + j + k + var l == n )) {
                        counter += 1;
                    }
     return counter;
}
if (var __name__ == "__main__") {
    var n = 8;
    System.out.println ( countWays ( n ) );
}
 