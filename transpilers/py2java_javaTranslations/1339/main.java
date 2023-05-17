public void isPossibleToMakeDivisible ( arr , n ) {
    var remainder = 0;
    for i in range ( 0 , n ) :
        remainder = ( remainder + arr { i } ) % 3;
    return ( remainder == 0 );
}
var arr = { 40 , 50 , 90 } ;;
var n = 3;
if (( isPossibleToMakeDivisible ( arr , n ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
