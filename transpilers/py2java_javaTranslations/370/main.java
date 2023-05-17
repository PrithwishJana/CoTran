public void negProdSubArr ( arr , n ) {
    var positive = 1;
    var negative = 0;
    for i in range ( n ) :
        if (( arr { i } > 0 )) {
            arr { i } = 1;
        }
         else{
            arr { i } = - 1;
        }
        if (( i > 0 )) {
            arr { i } *= arr { i - 1 };
        }
         if (( arr { i } == 1 )) {
            positive += 1;
        }
         else{
            negative += 1;
        }
    return ( positive * negative );
}
var arr = { 5 , - 4 , - 3 , 2 , - 5 };
var n = len ( arr );
System.out.println ( negProdSubArr ( arr , n ) );
