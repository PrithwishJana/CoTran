a , var b = ( int ( x ) for x in input ( ) . split ( ) );
var MAX = ( 1 << 32 ) - 1;
System.out.println ( "{:032b}" . format ( a & b ) );
System.out.println ( "{:032b}" . format ( a | b ) );
System.out.println ( "{:032b}" . format ( a ^ b ) );
