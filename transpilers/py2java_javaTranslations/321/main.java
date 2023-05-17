import math;
public void line2int ( linea ) {
    var temp = "";
    for (int i = 0; i < linea.length; i++){
        if (i == " ") {
            if (temp != "") {
                val1 = int ( temp );
                temp = "";
            }
         }
         else{
            temp = temp + i;
        }
    }
    var val2 = int ( temp );
    return ( val1 , val2 );
}
( n , t ) = line2int ( input ( ) );
for i in range ( n ) :
    ( salida , intervalo ) = line2int ( input ( ) );
    if (salida < t) {
        var salida = salida + ( math . ceil ( ( t - salida ) / intervalo ) * intervalo );
    }
     if (var i == 0) {
        var out = { i + 1 , salida };
    }
     else if (salida < out { 1 }){
        out = { i + 1 , salida };
    }
System.out.println ( out { 0 } );
