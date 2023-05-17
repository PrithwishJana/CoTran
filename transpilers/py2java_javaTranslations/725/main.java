public void LongestFibSubseq ( A , n ) {
    var S = set ( A );
    var maxLen = 0;
    for i in range ( 0 , n ) :
        for j in range ( i + 1 , n ) :
            x = A { j };
            y = A { i } + A { j };
            length = 2;
            while (y in S) {
                z = x + y;
                x = y;
                y = z;
                length += 1;
                maxLen = max ( maxLen , length );
            }
     return maxLen if maxLen >= 3 else 0;
}
if (var __name__ == "__main__") {
    var A = { 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 };
    var n = len ( A );
    System.out.println ( LongestFibSubseq ( A , n ) );
}
 