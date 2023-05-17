n , var m = map ( int , input ( ) . split ( ) );
var l = {};
for i in range ( n ) :
    var s = input ( );
    s = list ( s );
    for j in range ( m ) :
        if (s { j } == '.') {
            if ( i + j ) & 1 : s { j } = 'W';
            else : s { j } = 'B';
        }
     l . append ( s );
for c in l : System.out.println ( "" . join ( c ) );
