m , var r = map ( int , input ( ) . split ( ) );
res , var sq2 = 0 , ( 2 ** .5 );
for i in range ( 1 , m ) :
    res += 2 + sq2 + 2 * sq2 * ( i - 1 ) + ( i - 1 ) * i;
var res = ( res + m ) * 2 * r;
System.out.println ( res / ( m * m ) );
