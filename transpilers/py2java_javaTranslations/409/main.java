public void harmonicMean ( arr , freq , n ) {
    var sm = 0;
    frequency_sum = 0;
    for i in range ( 0 , n ) :
        sm = sm + freq { i } / arr { i };
        var frequency_sum = frequency_sum + freq { i };
    return ( round ( frequency_sum / sm , 4 ) );
}
var num = { 13 , 14 , 15 , 16 , 17 };
var freq = { 2 , 5 , 13 , 7 , 3 };
var n = len ( num );
System.out.println ( "{:.4f}" . format ( harmonicMean ( num , freq , n ) ) );
