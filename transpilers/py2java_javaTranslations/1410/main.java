public void Mean ( arr , n ) {
    var sm = 0;
    for i in range ( 0 , n ) :
        sm = sm + arr { i };
    return sm // n;
}
public void meanAbsoluteDeviation ( arr , n ) {
    var absSum = 0;
    for i in range ( 0 , n ) :
        absSum = absSum + abs ( arr { i } - Mean ( arr , n ) );
    return absSum / n;
}
var arr = { 10 , 15 , 15 , 17 , 18 , 21 };
var n = len ( arr );
System.out.println ( meanAbsoluteDeviation ( arr , n ) );
