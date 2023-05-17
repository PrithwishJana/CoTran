public void minOperations ( arr , n ) {
    var result = 0;
    var freq = { 0 } * 1000001;
    for i in range ( 0 , n ) :
        freq { arr [ i } ] += 1;
    var maxi = max ( arr );
    for i in range ( 1 , maxi + 1 ) :
        if (freq { i } != 0) {
            for j in range ( i * 2 , maxi + 1 , i ) :
                freq { j } = 0;
            result += 1;
        }
     return result;
}
if (var __name__ == "__main__") {
    var arr = { 2 , 4 , 2 , 4 , 4 , 4 };
    var n = len ( arr );
    System.out.println ( minOperations ( arr , n ) );
}
 