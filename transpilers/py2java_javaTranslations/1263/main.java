import math;
public void bitAtGivenPosSetOrUnset ( n , k ) {
    var new_num = n >> ( k - 1 );
    return ( new_num & 1 );
}
var n = 10;
var k = 2;
if (( bitAtGivenPosSetOrUnset ( n , k ) )) {
    System.out.println ( "Set" );
}
 else{
    System.out.println ( "Unset" );
}
