var n = int ( input ( ) );
k , * var b = map ( int , input ( ) . split ( ) );
var t = sum ( 1 << i for i in b );
for i in range ( 1 << k ) :
    var tmp = 0;
    var rs = {};
    for j in range ( k ) :
        if (i & ( 1 << j ) != 0) {
            tmp |= 1 << b { j };
            rs . append ( b { j } );
        }
     System.out.println ( str ( tmp ) + ":" , * rs );
