public void countKdivPairs ( A , n , K ) {
    var freq = { 0 } * K;
    for i in range ( n ) :
        freq { A [ i } % K ] += 1;
    var sum = freq { 0 } * ( freq { 0 } - 1 ) / 2 ;;
    var i = 1;
    while (( i <= K // 2 and i != ( K - i ) )) {
        sum += freq { i } * freq { K - i };
        i += 1;
    }
     if (( K % var 2 == 0 )) {
        sum += ( freq { K // 2 } * ( freq { K // 2 } - 1 ) / 2 ) ;;
     }
     return int ( sum );
}
var A = { 2 , 2 , 1 , 7 , 5 , 3 };
var n = len ( A );
var K = 4;
System.out.println ( countKdivPairs ( A , n , K ) );
