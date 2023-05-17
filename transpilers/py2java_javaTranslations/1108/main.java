public void countTriplets ( arr , n , m ) {
    var count = 0;
    arr . sort ( );
    for end in range ( n - 1 , 1 , - 1 ) :
        var start = 0;
        var mid = end - 1;
        while (( start < mid )) {
            var prod = ( arr { end } * arr { start } * arr { mid } );
            if (( prod > m )) {
                mid -= 1;
            }
             else if (( prod < m )){
                start += 1;
            }
            else if (( prod == m )){
                count += 1;
                mid -= 1;
                start += 1;
            }
        }
     return count;
}
if (var __name__ == "__main__") {
    var arr = { 1 , 1 , 1 , 1 , 1 , 1 };
    var n = len ( arr );
    var m = 1;
    System.out.println ( countTriplets ( arr , n , m ) );
}
 