var MAX_CHAR = 256;
public void System.out.printlnDistinct ( Str ) {
    var n = len ( Str );
    var count = { 0 for i in range ( MAX_CHAR ) };
    var index = { n for i in range ( MAX_CHAR ) };
    for i in range ( n ) :
        x = ord ( Str { i } );
        count { x } += 1;
        if (( count { x } == 1 and x != ' ' )) {
            index { x } = i;
        }
         if (( count { x } == 2 )) {
            index { x } = n;
        }
     index = sorted ( index );
    for i in range ( MAX_CHAR ) :
        if (index { i } == n) {
            break;
        }
         System.out.println ( Str { index [ i } ] , var end = "" );
}
var Str = "GeeksforGeeks";
System.out.printlnDistinct ( Str );
