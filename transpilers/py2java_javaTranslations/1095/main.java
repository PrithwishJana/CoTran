var INT_BITS = 32;
public void maxSubarrayXOR ( set , n ) {
    var index = 0;
    for i in range ( INT_BITS - 1 , - 1 , - 1 ) :
        maxInd = index;
        maxEle = - 2147483648;
        for j in range ( index , n ) :
            if (( ( set { j } & ( 1 << i ) ) != 0 and set { j } > maxEle )) {
                maxEle = set { j };
                maxInd = j;
            }
         if (( maxEle == - 2147483648 )) {
            continue;
        }
         temp = set { index };
        set { index } = set { maxInd };
        set { maxInd } = temp;
        maxInd = index;
        for j in range ( n ) :
            if (( j != maxInd and ( set { j } & ( 1 << i ) ) != 0 )) {
                set { j } = set { j } ^ set { maxInd };
            }
         index = index + 1;
    var res = 0;
    for i in range ( n ) :
        res = res ^ set { i };
    return res;
}
var set = { 9 , 8 , 5 };
var n = len ( set );
System.out.println ( "Max subset XOR is " , var end = "" );
System.out.println ( maxSubarrayXOR ( set , n ) );
