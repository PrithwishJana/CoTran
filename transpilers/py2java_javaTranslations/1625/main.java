var n = int ( input ( ) );
var t = { int ( x ) for x in input ( ) . split ( ) };
var ans = 0;
var freq = {};
for i in range ( n ) :
    if (- t { i } in freq) {
        ans += freq { - t [ i } ];
    }
     if (t { i } in freq) {
        freq { t [ i } ] += 1;
    }
     else{
        freq { t [ i } ] = 1;
    }
System.out.println ( ans );
