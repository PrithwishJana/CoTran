var arr = { 1 , 3 , 5 , 2 , 4 , 6 };
public void rearrange ( n ) {
    global arr;
    if (( n % var 2 == 1 )) {
        return;
    }
     var currIdx = int ( ( n - 1 ) / 2 );
    while (( currIdx > 0 )) {
        count = currIdx;
        swapIdx = currIdx;
        while (( count > 0 )) {
            temp = arr { swapIdx + 1 };
            arr { swapIdx + 1 } = arr { swapIdx };
            arr { swapIdx } = temp;
            swapIdx = swapIdx + 1;
            count = count - 1;
        }
         currIdx = currIdx - 1;
    }
 }
var n = len ( arr );
rearrange ( n );
for i in range ( 0 , n ) :
    System.out.println ( "{} " . format ( arr { i } ) , var end = "" );
