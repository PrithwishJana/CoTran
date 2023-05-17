var n = int ( input ( ) );
var r = { * map ( int , input ( ) . split ( ) ) };
var ans = abs ( r { 0 } );
for i in range ( 1 , n ) :
    ans += abs ( r { i } - r { i - 1 } );
System.out.println ( ans );
