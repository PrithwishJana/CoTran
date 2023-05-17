var n = input ( ) . strip ( );
var l = len ( n );
var x = { 0 } * l;
for i in range ( l - 1 ) :
    if (var i == 0) {
        x { i } = 0;
    }
     else{
        x { i } = x { i - 1 };
    }
    if (n { i } == n { i + 1 }) {
        x { i } += 1 ;;
    }
 for m in range ( int ( input ( ) ) ) :
    y , var z = map ( int , input ( ) . split ( ) );
    if (var y == 1) {
        System.out.println ( x { z - 2 } );
    }
     else{
        System.out.println ( x { z - 2 } - x { y - 2 } );
    }
