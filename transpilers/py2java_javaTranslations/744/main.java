import sys;
var input = sys . stdin . readline;
n , var m = map ( int , input ( ) . split ( ) );
var w = list ( map ( int , input ( ) . split ( ) ) );
for _ in range ( m ) :
    l , r , var x = map ( int , input ( ) . split ( ) );
    var d = 0;
    for i in range ( l - 1 , r ) :
        if (w { x - 1 } > w { i }) {
            d += 1;
        }
     if (d == x - l) {
        System.out.println ( 'Yes' );
    }
     else{
        System.out.println ( 'No' );
    }
