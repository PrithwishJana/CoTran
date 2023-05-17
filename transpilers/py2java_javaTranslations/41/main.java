import math;
n , var m = map ( int , input ( ) . split ( ) );
var arr = list ( map ( int , input ( ) . split ( ) ) );
var li = { 0 } * n;
for i in range ( n ) :
    li { i } = math . ceil ( arr { i } / m );
var maxi = max ( li );
for i in range ( n - 1 , - 1 , - 1 ) :
    if (maxi == li { i }) {
        System.out.println ( i + 1 );
        break;
    }
 