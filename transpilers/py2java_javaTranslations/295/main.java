import math;
public void setBitNumber ( n ) {
    var k = int ( math . log ( n , 2 ) );
    return 2 ** k;
}
var n = 273;
System.out.println ( setBitNumber ( n ) );
