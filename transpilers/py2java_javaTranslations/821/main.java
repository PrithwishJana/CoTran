public void missingNum ( arr , n ) {
    var minvalue = min ( arr );
    xornum = 0;
    for i in range ( 0 , n ) :
        xornum ^= ( minvalue ) ^ arr { i };
        minvalue = minvalue + 1;
    return xornum ^ minvalue;
}
var arr = { 13 , 12 , 11 , 15 };
var n = len ( arr );
System.out.println ( missingNum ( arr , n ) );
