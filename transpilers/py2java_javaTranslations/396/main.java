public void ReplaceElements ( arr , n ) {
    if (n <= 1) {
        return;
    }
     var prev = arr { 0 };
    arr { 0 } = arr { 0 } ^ arr { 1 };
    for i in range ( 1 , n - 1 ) :
        curr = arr { i };
        arr { i } = prev ^ arr { i + 1 };
        prev = curr;
    arr { n - 1 } = prev ^ arr { n - 1 };
}
var arr = { 2 , 3 , 4 , 5 , 6 };
var n = len ( arr );
ReplaceElements ( arr , n );
for i in range ( n ) :
    System.out.println ( arr { i } , var end = " " );
