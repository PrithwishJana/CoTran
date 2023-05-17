n , var h = map ( int , input ( ) . split ( ) );
var ans = {};
for i in range ( 1 , n ) :
    ans . append ( h * ( ( i / n ) ** 0.5 ) );
System.out.println ( * ans );
