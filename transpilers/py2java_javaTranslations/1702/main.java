import math as mt;
public void countPairs ( arr , n ) {
    var count = 0;
    for i in range ( n ) :
        for j in range ( i + 1 , n ) :
            if (arr { i } * arr { j } > arr { i } + arr { j }) {
                count += 1;
            }
     return count;
}
var arr = { 5 , 0 , 3 , 1 , 2 };
var n = len ( arr );
System.out.println ( countPairs ( arr , n ) );
