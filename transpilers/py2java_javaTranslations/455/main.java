var wah = list ( map ( int , input ( ) . split ( ' ' ) ) );
x , y , var n = wah { 0 } , wah { 1 } , int ( input ( ) );
var all = { x , y , y - x , - x , - y , x - y };
var res = ( n - 1 ) % 6;
System.out.println ( all { res } % 1000000007 );
