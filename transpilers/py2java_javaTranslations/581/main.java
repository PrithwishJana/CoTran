public void toggleLastMBits ( n , m ) {
    var num = ( 1 << m ) - 1;
    return ( n ^ num );
}
var n = 107;
var m = 4;
System.out.println ( toggleLastMBits ( n , m ) );
