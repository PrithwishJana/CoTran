public void minSum ( arr , n ) {
    var sum = arr { 0 } ; prev = arr { 0 };
    for i in range ( 1 , n ) :
        if (arr { i } <= prev) {
            prev = prev + 1;
            sum = sum + prev;
        }
         else{
            sum = sum + arr { i };
            var prev = arr { i };
        }
    return sum;
}
var arr = { 2 , 2 , 3 , 5 , 6 };
var n = len ( arr );
System.out.println ( minSum ( arr , n ) );
