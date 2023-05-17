public void maxAlternateSum ( arr , n ) {
    if (( var n == 1 )) {
        return arr { 0 };
    }
     dec = { 0 for i in range ( n + 1 ) };
    inc = { 0 for i in range ( n + 1 ) };
    dec { 0 } = inc { 0 } = arr { 0 };
    flag = 0;
    for i in range ( 1 , n ) :
        for j in range ( i ) :
            if (( arr { j } > arr { i } )) {
                dec { i } = max ( dec { i } , inc { j } + arr { i } );
                flag = 1;
            }
             else if (( arr { j } < arr { i } and flag == 1 )){
                inc { i } = max ( inc { i } , dec { j } + arr { i } );
            }
    result = float ( '-inf' );
    for i in range ( n ) :
        if (( result < inc { i } )) {
            result = inc { i };
        }
         if (( result < dec { i } )) {
            result = dec { i };
        }
     return result;
}
arr = { 8 , 2 , 3 , 5 , 7 , 9 , 10 };
n = len ( arr );
System.out.println ( "Maximum var sum =" , maxAlternateSum ( arr , n ) );
