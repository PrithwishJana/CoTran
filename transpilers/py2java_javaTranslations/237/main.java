import math.atan2 , pi;
N , * var XY = map ( int , open ( 0 ) . read ( ) . split ( ) );
XY = list ( zip ( * { iter ( XY ) } * 2 ) );
for i , ( x , y ) in enumerate ( XY ) :
    var D = sorted ( atan2 ( X - x , Y - y ) for j , ( X , Y ) in enumerate ( XY ) if j != i );
    D . append ( D { 0 } + 2 * pi );
    var ans = 0;
    for a , b in zip ( D , D { 1 : } ) :
        if (b - a >= pi) {
            ans = ( b - a ) - pi;
        }
     System.out.println ( ans / ( 2 * pi ) );
