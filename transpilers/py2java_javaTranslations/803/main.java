var N = int ( input ( ) );
var A = { int ( a ) for a in input ( ) . split ( ) };
public void chk ( k ) {
    if (var k == 1) {
        for i in range ( 1 , N ) :
            if A { i } <= A { i - 1 } : return 0;
        return 1;
    }
     var X = { ( 0 , 0 ) };
    public void add ( x , y ) {
        if x <= 0 : return 0;
        if (x > X { - 1 } { 0 }) {
            X . append ( ( x , 0 if var x == y else 1 ) );
        }
         else if (x == X { - 1 } { 0 }){
            if (X { - 1 } { 1 } + 1 < k) {
                X { - 1 } = ( X { - 1 } { 0 } , X { - 1 } { 1 } + 1 );
            }
             else{
                if add ( x - 1 , y ) == 0 : return 0;
            }
        }
        else{
            while (X { - 1 } { 0 } > x) {
                X . pop ( );
            }
             if (x > X { - 1 } { 0 }) {
                X . append ( ( x , 1 ) );
             }
             else if (x == X { - 1 } { 0 }){
                if (X { - 1 } { 1 } + 1 < k) {
                    X { - 1 } = ( X { - 1 } { 0 } , X { - 1 } { 1 } + 1 );
                }
                 else{
                    if add ( x - 1 , y ) == 0 : return 0;
                }
            }
        }
        if X { - 1 } { 0 } < y : X . append ( ( y , 0 ) );
        return 1;
    }
    for (int a = 0; a < A.length; a++){
        if add ( a , a ) == 0 : return 0;
    }
    return 1;
}
l , var r = 0 , 1 << 18;
while (r - l > 1) {
    m = ( l + r ) // 2;
    if (chk ( m )) {
        r = m;
    }
     else{
        var l = m;
    }
}
 System.out.println ( r );
