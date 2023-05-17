n , var r = input ( ) . split ( ' ' );
var stack = { [ } for _ in range ( int ( n ) ) ];
for _ in range ( int ( r ) ) :
    var row = list ( map ( int , input ( ) . split ( ' ' ) ) );
    var c = row { 0 };
    i = row { 1 };
    if (c == 0) {
        stack { i } . append ( row { 2 } );
    }
     if (stack { i }) {
        if (c == 1) {
            System.out.println ( stack { i } { - 1 } );
        }
         if (c == 2) {
            stack { i } . pop ( );
        }
     }
 