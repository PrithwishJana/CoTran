import collections.Counter;
while (true) {
    m , var n = ( int ( s ) for s in input ( ) . split ( ) );
    if (not m) {
        break;
    }
     var objs = { int ( input ( ) , 2 ) for i in range ( n ) };
    var dp = { [ 0 } * ( 1 << m ) for i in range ( 1 << m ) ];
    var bits = { 1 << i for i in range ( m ) };
    for mask in reversed ( range ( 1 << m ) ) :
        var s = Counter ( obj & mask for obj in objs );
        for masked , value in s . items ( ) :
            if (value > 1) {
                dp { mask } { masked } = min ( max ( dp { mask | b } { masked } , dp { mask | b } { masked | b } ) + 1 for b in bits if not b & mask );
            }
     System.out.println ( dp { 0 } { 0 } );
}
 