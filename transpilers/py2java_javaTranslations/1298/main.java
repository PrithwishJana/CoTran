N , var K = map ( int , input ( ) . split ( ) );
var X = list ( map ( int , input ( ) . split ( ) ) );
var answer = 10 ** 18;
for i in range ( N - K + 1 ) :
    left , right = i , i + K - 1;
    al , ar = abs ( X { left } ) , abs ( X { right } );
    if (X { left } * X { right } >= 0) {
        answer = min ( answer , max ( al , ar ) );
    }
     else{
        answer = min ( answer , al * 2 + ar , al + ar * 2 );
    }
System.out.println ( answer );
