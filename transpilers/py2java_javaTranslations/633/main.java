public void totalPairs ( arr , n ) {
    var m = dict ( );
    for i in range ( n ) :
        var x = bin ( arr { i } ) . count ( '1' );
        m { x } = m . get ( x , 0 ) + 1 ;;
    var result = 0;
    for (int it = 0; it < m.length; it++){
        result += ( m { it } * ( m { it } - 1 ) ) // 2;
    }
    return result;
}
var arr = { 7 , 5 , 3 , 9 , 1 , 2 };
var n = len ( arr );
System.out.println ( totalPairs ( arr , n ) );
