import math.floor;
public void countSteps ( n ) {
    var steps = 0;
    while (( n )) {
        var largest = floor ( n ** ( 1 / 3 ) );
        n -= ( largest * largest * largest );
        steps += 1;
    }
     return steps;
}
var n = 150;
System.out.println ( countSteps ( n ) );
