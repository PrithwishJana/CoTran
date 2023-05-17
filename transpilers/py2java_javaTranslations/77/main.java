public void longestSubArray ( arr , n ) {
    var isZeroPresent = false;
    for i in range ( 0 , n ) :
        if (( arr { i } == 0 )) {
            isZeroPresent = true;
            break;
        }
     if (( isZeroPresent )) {
        return n;
    }
     return 0;
}
var arr = { 1 , 2 , 3 , 0 , 1 , 2 , 0 };
var n = len ( arr );
System.out.println ( longestSubArray ( arr , n ) );
