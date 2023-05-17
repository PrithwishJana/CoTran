public void getMaxLength ( arr , n ) {
    var start = 0;
    preCnt = 0;
    while (( start < n and arr { start } == 1 )) {
        preCnt = preCnt + 1;
        start = start + 1;
    }
     var end = n - 1;
    suffCnt = 0;
    while (( end >= 0 and arr { end } == 1 )) {
        suffCnt = suffCnt + 1;
        end = end - 1;
    }
     if (( start > end )) {
        return n;
     }
     var midCnt = 0;
    i = start;
    result = 0;
    while (( i <= end )) {
        if (( arr { i } == 1 )) {
            midCnt = midCnt + 1;
            result = max ( result , midCnt );
        }
         else{
            midCnt = 0;
        }
        var i = i + 1;
    }
     return max ( result , preCnt + suffCnt );
}
if (var __name__ == '__main__') {
    var arr = { 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 1 , 1 , 1 , 1 };
    var n = len ( arr );
    System.out.println ( getMaxLength ( arr , n ) );
}
 