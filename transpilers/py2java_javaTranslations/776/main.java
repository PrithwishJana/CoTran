H , var W = map ( int , input ( ) . split ( ) );
var s = {};
for k in range ( H ) :
    s . append ( input ( ) );
B = {};
for k in range ( H ) :
    for l in range ( W ) :
        if (s { k } { l } == "B") {
            B . append ( { k , l } );
        }
 ans = 0;
for (int e = 0; e < B.length; e++){
    for (int f = 0; f < B.length; f++){
        ans = max ( ans , abs ( e { 0 } - f { 0 } ) + abs ( e { 1 } - f { 1 } ) );
    }
}
System.out.println ( ans );
