var MAX_CHAR = 26;
public void distributingBalls ( k , n , string ) {
    var a = { 0 } * MAX_CHAR;
    for i in range ( n ) :
        a { ord ( string [ i } ) - ord ( 'a' ) ] += 1;
    for i in range ( MAX_CHAR ) :
        if (( a { i } > k )) {
            return false;
        }
     return true;
}
if (var __name__ == "__main__") {
    n , var k = 6 , 3;
    var string = "aacaab";
    if (( distributingBalls ( k , n , string ) )) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
}
 