public void subsetPairNotDivisibleByK ( arr , N , K ) {
    var f = { 0 for i in range ( K ) };
    for i in range ( N ) :
        f { arr [ i } % K ] += 1;
    if (( K % var 2 == 0 )) {
        f { K // 2 } = min ( f { K // 2 } , 1 );
    }
     var res = min ( f { 0 } , 1 );
    for i in range ( 1 , ( K // 2 ) + 1 ) :
        res += max ( f { i } , f { K - i } );
    return res;
}
var arr = { 3 , 7 , 2 , 9 , 1 };
var N = len ( arr );
var K = 3;
System.out.println ( subsetPairNotDivisibleByK ( arr , N , K ) );
