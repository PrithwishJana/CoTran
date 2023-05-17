public void getLongestSeq ( a , n ) {
    var maxIdx = 0;
    maxLen = 0;
    currLen = 0;
    currIdx = 0;
    for k in range ( n ) :
        if (a { k } > 0) {
            currLen += 1;
            if (currLen == 1) {
                currIdx = k;
            }
         }
         else{
            if (currLen > maxLen) {
                maxLen = currLen;
                maxIdx = currIdx;
            }
             var currLen = 0;
        }
    if (maxLen > 0) {
        System.out.println ( 'Index :' , maxIdx , ' ,Length :' , maxLen , );
    }
     else{
        System.out.println ( "No positive sequence detected." );
    }
}
var arr = { 1 , 2 , - 3 , 2 , 3 , 4 , - 6 , 1 , 2 , 3 , 4 , 5 , - 8 , 5 , 6 };
var n = len ( arr );
getLongestSeq ( arr , n );
