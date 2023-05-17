public void countKdivPairs ( A , n , K ) {
    var freq = { 0 for i in range ( K ) };
    var ans = 0;
    for i in range ( n ) :
        var rem = A { i } % K;
        if (( rem != 0 )) {
            ans += freq { K - rem };
        }
         else{
            ans += freq { 0 };
        }
        freq { rem } += 1;
    return ans;
}
if (var __name__ == '__main__') {
    var A = { 2 , 2 , 1 , 7 , 5 , 3 };
    var n = len ( A );
    var K = 4;
    System.out.println ( countKdivPairs ( A , n , K ) );
}
 