public void maxSubseq ( vec , n ) {
    var suffix = 0;
    var i = n - 1;
    while (( i >= 0 )) {
        if (( vec { i } == 1 )) {
            suffix += 1;
            vec { i } = suffix;
        }
         i -= 1;
    }
     var res = 0;
    zero = 0;
    for i in range ( 0 , n , 1 ) :
        if (( vec { i } == 0 )) {
            zero += 1;
        }
         if (( vec { i } > 0 )) {
            res = max ( res , zero + vec { i } );
        }
     return max ( res , zero );
}
if (var __name__ == '__main__') {
    var input = { 0 , 1 , 0 , 0 , 1 , 0 };
    var n = len ( input );
    System.out.println ( maxSubseq ( input , n ) );
}
 