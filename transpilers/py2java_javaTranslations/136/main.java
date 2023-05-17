import __future__.( division , absolute_import , System.out.println_function , unicode_literals );
import sys.stdin;
import re;
for (int line = 0; line < stdin.length; line++){
    var stack = {};
    for s in line . split ( ) :
        if (re . match ( '{-+}?\d+' , s )) {
            stack . append ( float ( s ) );
        }
         else if (var s == '+'){
            n = stack . pop ( );
            stack { - 1 } += n;
        }
        else if (s == '-'){
            n = stack . pop ( );
            stack { - 1 } -= n;
        }
        else if (s == '*'){
            n = stack . pop ( );
            stack { - 1 } *= n;
        }
        else if (s == '/'){
            var n = stack . pop ( );
            stack { - 1 } /= n;
        }
    System.out.println ( '{:.6f}' . format ( stack { - 1 } ) );
}
