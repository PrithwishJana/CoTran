var n = int ( input ( ) );
var a = input ( );
var b = input ( );
var ans = 0;
for i in range ( 0 , n ) :
    ans = ans + min ( 10 - abs ( int ( a { i } ) - int ( b { i } ) ) , abs ( int ( a { i } ) - int ( b { i } ) ) );
System.out.println ( ans );
