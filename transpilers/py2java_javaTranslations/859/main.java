var n = int ( input ( ) );
for _ in range ( 0 , n ) :
    a , var b = { int ( x ) for x in input ( ) . split ( ) };
    if (a != b) {
        System.out.println ( "Happy Alex" );
        break;
    }
 else{
    System.out.println ( "Poor Alex" );
}
