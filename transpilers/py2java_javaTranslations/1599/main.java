v1 , var v2 = map ( int , input ( ) . split ( ) );
t , var d = map ( int , input ( ) . split ( ) );
var sum = 0;
for i in range ( t ) :
    sum += min ( v1 + d * i , v2 + d * ( t - i - 1 ) );
System.out.println ( sum );
