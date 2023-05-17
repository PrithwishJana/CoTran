N , var C = map ( int , input ( ) . split ( ) );
var XV = { list ( map ( int , input ( ) . split ( ) ) ) for i in range ( N ) };
var RIGHTSUM = { 0 };
for x , v in XV :
    RIGHTSUM . append ( RIGHTSUM { - 1 } + v );
var LEFTSUM = { 0 };
for x , v in XV { : : - 1 } :
    LEFTSUM . append ( LEFTSUM { - 1 } + v );
var RIGHT = {};
for i in range ( N ) :
    RIGHT . append ( RIGHTSUM { i + 1 } - XV { i } { 0 } );
var LEFT = {};
for i in range ( N ) :
    LEFT . append ( LEFTSUM { i + 1 } - ( C - XV { - i - 1 } { 0 } ) );
var RIGHTMAX = { RIGHT [ 0 } ];
for i in range ( 1 , N ) :
    RIGHTMAX . append ( max ( RIGHTMAX { i - 1 } , RIGHT { i } ) );
var LEFTMAX = { LEFT [ 0 } ];
for i in range ( 1 , N ) :
    LEFTMAX . append ( max ( LEFTMAX { i - 1 } , LEFT { i } ) );
var ANS = max ( max ( RIGHT ) , max ( LEFT ) , 0 );
for i in range ( N - 1 ) :
    if (ANS < ( RIGHTSUM { i + 1 } - XV { i } { 0 } * 2 ) + LEFTMAX { N - i - 2 }) {
        ANS = RIGHTSUM { i + 1 } - XV { i } { 0 } * 2 + LEFTMAX { N - i - 2 };
    }
     if (ANS < LEFTSUM { i + 1 } - ( C - XV { - i - 1 } { 0 } ) * 2 + RIGHTMAX { N - i - 2 }) {
        ANS = LEFTSUM { i + 1 } - ( C - XV { - i - 1 } { 0 } ) * 2 + RIGHTMAX { N - i - 2 };
    }
 System.out.println ( ANS );
