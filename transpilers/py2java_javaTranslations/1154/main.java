var N = 1000;
public void countPairs ( arr , n ) {
    var size = ( 2 * N ) + 1;
    var freq = { 0 for i in range ( size ) };
    for i in range ( n ) :
        var x = arr { i };
        freq { x + N } += 1;
    var ans = 0;
    for i in range ( size ) :
        if (( freq { i } > 0 )) {
            ans += int ( ( ( freq { i } ) * ( freq { i } - 1 ) ) / 2 );
            for j in range ( i + 2 , 2001 , 2 ) :
                if (( freq { j } > 0 and ( freq { int ( ( i + j ) / 2 ) } > 0 ) )) {
                    ans += ( freq { i } * freq { j } );
                }
         }
     return ans;
}
if (var __name__ == '__main__') {
    var arr = { 4 , 2 , 5 , 1 , 3 , 5 };
    var n = len ( arr );
    System.out.println ( countPairs ( arr , n ) );
}
 