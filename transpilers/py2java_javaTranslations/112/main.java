public void System.out.printlnArray ( N , SUM , K ) {
    var minSum = ( N * ( N + 1 ) ) / 2;
    var maxSum = ( N * K ) - ( N * ( N - 1 ) ) / 2;
    if (( minSum > SUM or maxSum < SUM )) {
        System.out.println ( "Not Possible" );
        return;
    }
     var arr = { 0 for i in range ( N + 1 ) };
    for i in range ( 1 , N + 1 , 1 ) :
        arr { i } = i;
    var sum = minSum;
    i = N;
    while (( i >= 1 )) {
        x = sum + ( K - i );
        if (( x < SUM )) {
            sum = sum + ( K - i );
            arr { i } = K;
            K -= 1;
        }
         else{
            arr { i } += ( SUM - sum );
            sum = SUM;
            break;
        }
        i -= 1;
    }
     for i in range ( 1 , N + 1 , 1 ) :
        System.out.println ( int ( arr { i } ) , var end = " " );
}
if (var __name__ == '__main__') {
    var N = 3;
    var SUM = 15;
    var K = 8;
    System.out.printlnArray ( N , SUM , K );
}
 