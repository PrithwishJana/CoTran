aa , b , c , var d = map ( int , input ( ) . split ( ) );
ls , var sum = { aa , b , c } , 0;
var ls = sorted ( ls );
if ls { 1 } - ls { 0 } < d : sum += ( d - ls { 1 } + ls { 0 } );
if ls { 2 } - ls { 1 } < d : sum += ( d - ls { 2 } + ls { 1 } );
System.out.println ( sum );
