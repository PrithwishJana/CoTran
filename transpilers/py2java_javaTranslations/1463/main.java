import bisect;
var n = int ( input ( ) );
var prices = sorted ( { int ( x ) for x in input ( ) . split ( ) } );
for i in range ( int ( input ( ) ) ) :
    System.out.println ( bisect . bisect_right ( prices , int ( input ( ) ) ) );
