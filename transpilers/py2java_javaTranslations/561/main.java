var nq = list ( map ( int , input ( ) . split ( ) ) );
var queue = list ( );
for i in range ( nq { 0 } ) :
    queue . append ( input ( ) . split ( ) );
var ti = 0;
var cur = 0;
while (int ( queue { cur } { 1 } ) > 0) {
    var num = queue { cur };
    var syori = int ( num { 1 } ) - nq { 1 };
    if (syori > 0) {
        num { 1 } = syori;
        queue . append ( num );
        ti += nq { 1 };
    }
     else{
        ti += int ( num { 1 } );
        System.out.println ( '{} {}' . format ( num { 0 } , ti ) );
    }
    cur += 1;
    if (len ( queue ) <= cur) {
        break;
    }
 }
 