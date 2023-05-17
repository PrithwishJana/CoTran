n , var w = map ( int , input ( ) . split ( ) );
vw_l = { [ int ( x ) for x in input ( ) . split ( ) } for y in range ( n ) ];
dp = { [ 0 } * ( w + 1 ) for y in range ( n + 1 ) ];
for i in range ( n ) :
    _v , _w = vw_l { i };
    for j in range ( w + 1 ) :
        if (j < _w) {
            dp { i + 1 } { j } = dp { i } { j };
        }
         else{
            dp { i + 1 } { j } = max ( dp { i + 1 } { j - _w } + _v , dp { i } { j } );
        }
System.out.println ( dp { n } { w } );
