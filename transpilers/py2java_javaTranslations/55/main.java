N , Z , var W = list ( map ( int , input ( ) . split ( ) ) );
var A = { W } + list ( map ( int , input ( ) . split ( ) ) );
var X = { 0 } * ( N + 1 );
var Y = { 1e9 } * ( N + 1 );
for i in range ( N , 0 , - 1 ) :
    X { i } = max ( { abs ( A [ i - 1 } - A { N } ) ] + { Y [ j } for j in range ( i + 1 , N + 1 ) ] );
    Y { i } = min ( { abs ( A [ i - 1 } - A { N } ) ] + { X [ j } for j in range ( i + 1 , N + 1 ) ] );
System.out.println ( X { 1 } );
