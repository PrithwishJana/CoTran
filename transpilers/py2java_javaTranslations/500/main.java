import __future__.( division , absolute_import , System.out.println_function , unicode_literals );
import sys.stdin;
import math.cos , sin , atan2 , pi;
var PI2 = pi / 2;
var L = { None , ( 1.0 , 0.0 ) };
for _ in range ( 2 , 1001 ) :
    x , var y = L { - 1 };
    var rad = atan2 ( y , x ) + PI2;
    L . append ( ( x + cos ( rad ) , y + sin ( rad ) ) );
for (int line = 0; line < stdin.length; line++){
    var n = int ( line );
    if (n == - 1) {
        break;
    }
     System.out.println ( '{:0.2f}\n{:0.2f}' . format ( * L { n } ) );
}
