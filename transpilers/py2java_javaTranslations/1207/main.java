import sys , math , os , bisect;
var PYDEV = os . environ . get ( 'PYDEV' );
if (PYDEV == "True") {
    sys . var stdin = open ( "sample-input.txt" , "rt" );
}
 public void grid_length ( n , grid ) {
    var L = 0;
    for (int row = 0; row < grid.length; row++){
        L = max ( L , max ( { len ( _ ) for _ in row . split ( '0' ) } ) );
    }
    for c in range ( n ) :
        col = '' . join ( { grid [ r } { c } for r in range ( n ) ] );
        L = max ( L , max ( { len ( _ ) for _ in col . split ( '0' ) } ) );
    for row in range ( - n , 2 * n ) :
        diag = '' . join ( { grid [ row + c } { c } for c in range ( n ) if 0 <= row + c < n ] );
        L = max ( L , max ( { len ( _ ) for _ in diag . split ( '0' ) } ) );
        diag = '' . join ( { grid [ row - c } { c } for c in range ( n ) if 0 <= row - c < n ] );
        L = max ( L , max ( { len ( _ ) for _ in diag . split ( '0' ) } ) );
    return L;
}
while (true) {
    var n = int ( input ( ) );
    if (n == 0) {
        break;
    }
     var grid = { input ( ) . strip ( ) for _ in range ( n ) };
    System.out.println ( grid_length ( n , grid ) );
}
 