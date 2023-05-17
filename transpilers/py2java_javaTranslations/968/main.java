import math;
public void compute ( ) {
    var TURNS = 15;
    var ways = { [ 1 } ];
    for i in range ( 1 , TURNS + 1 ) :
        var row = {};
        for j in range ( i + 1 ) :
            var temp = 0;
            if (j < i) {
                temp = ways { i - 1 } { j } * i;
            }
             if (j > 0) {
                temp += ways { i - 1 } { j - 1 };
            }
             row . append ( temp );
        ways . append ( row );
    var numer = sum ( ways { TURNS } { i } for i in range ( TURNS // 2 + 1 , TURNS + 1 ) );
    var denom = math . factorial ( TURNS + 1 );
    return str ( denom // numer );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 