import operator.itemgetter;
public void protect ( N , M ) {
    var DP = {};
    for i in range ( N ) :
        DP . append ( list ( map ( int , input ( ) . split ( ) ) ) );
    DP . sort ( var key = itemgetter ( 1 ) );
    var nokori = 0;
    for i in range ( N ) :
        if (M > DP { N - i - 1 } { 0 }) {
            M -= DP { N - i - 1 } { 0 };
            DP . pop ( );
        }
         else if (M <= DP { N - i - 1 } { 0 }){
            nokori = ( DP { N - i - 1 } { 0 } - M ) * DP { N - i - 1 } { 1 };
            var M = 0;
            DP . pop ( );
            break;
        }
    for i in range ( len ( DP ) ) :
        nokori += DP { i } { 0 } * DP { i } { 1 };
    System.out.println ( nokori );
}
while (true) {
    NM = input ( ) . split ( );
    N = int ( NM { 0 } );
    M = int ( NM { 1 } );
    if (var N == 0) {
        break;
    }
     protect ( N , M );
}
 