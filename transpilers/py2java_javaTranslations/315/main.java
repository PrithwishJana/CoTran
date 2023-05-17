N , M , var X = map ( int , input ( ) . split ( ) );
var A = sum ( int ( i ) < X for i in input ( ) . split ( ) );
System.out.println ( min ( A , M - A ) );
