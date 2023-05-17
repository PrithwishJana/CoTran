public void getTotalXorOfSubarrayXors ( arr , N ) {
    if (( N % var 2 == 0 )) {
        return 0;
    }
     var res = 0;
    for i in range ( 0 , N , 2 ) :
        res ^= arr { i };
    return res;
}
if (var __name__ == "__main__") {
    var arr = { 3 , 5 , 2 , 4 , 6 };
    var N = len ( arr );
    System.out.println ( getTotalXorOfSubarrayXors ( arr , N ) );
}
 