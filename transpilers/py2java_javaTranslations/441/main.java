import sys.stdin , stdout;
var input = stdin . readline;
var n = int ( input ( ) ) ; sa = sg = 0;
for i in range ( n ) :
    a , var g = map ( int , input ( ) . split ( ) );
    if (a <= g) {
        if (sa + a - sg <= 500) {
            sa += a ; stdout . write ( "A" );
        }
         else{
            sg += g ; stdout . write ( "G" );
        }
    }
     else{
        if (sg + g - sa <= 500) {
            sg += g ; stdout . write ( "G" );
        }
         else{
            sa += a ; stdout . write ( "A" );
        }
    }
