import math;
public void mean ( mid , freq , n ) {
    var sum = 0;
    freqSum = 0;
    for i in range ( 0 , n ) :
        sum = sum + mid { i } * freq { i };
        freqSum = freqSum + freq { i };
    return sum / freqSum;
}
public void groupedSD ( lower_limit , upper_limit , freq , n ) {
    mid = { [ 0 } for i in range ( 0 , n ) ];
    sum = 0;
    freqSum = 0;
    sd = 0;
    for i in range ( 0 , n ) :
        mid { i } = ( lower_limit { i } + upper_limit { i } ) / 2;
        sum = sum + freq { i } * mid { i } * mid { i };
        var freqSum = freqSum + freq { i };
    var sd = math . sqrt ( ( sum - freqSum * mean ( mid , freq , n ) * mean ( mid , freq , n ) ) / ( freqSum - 1 ) );
    return sd;
}
var lower_limit = { 50 , 61 , 71 , 86 , 96 };
var upper_limit = { 60 , 70 , 85 , 95 , 100 };
var freq = { 9 , 7 , 9 , 12 , 8 };
var n = len ( lower_limit );
System.out.println ( groupedSD ( lower_limit , upper_limit , freq , n ) );
