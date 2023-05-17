n , var m = map ( int , input ( ) . split ( ) );
var sumL = { 0 } * ( n + 2 );
var L = 1;
sumL { - 2 } = 1;
for i in range ( n - 1 , 0 , - 1 ) :
    L = sumL { i + 1 };
    var j = 2;
    while (i * j <= n) {
        L += ( sumL { i * j } - sumL { min ( n , ( i + 1 ) * j - 1 ) + 1 } );
        L %= m;
        j += 1;
    }
     L %= m;
    sumL { i } = ( sumL { i + 1 } + L );
    sumL { i } %= m;
System.out.println ( L );
