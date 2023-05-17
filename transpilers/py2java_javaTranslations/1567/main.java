public void mostFrequent ( arr , n ) {
    arr . sort ( );
    var max_count = 1 ; res = arr { 0 } ; curr_count = 1;
    for i in range ( 1 , n ) :
        if (( arr { i } == arr { i - 1 } )) {
            curr_count += 1;
        }
         else{
            if (( curr_count > max_count )) {
                max_count = curr_count;
                res = arr { i - 1 };
            }
             curr_count = 1;
        }
    if (( curr_count > max_count )) {
        max_count = curr_count;
        var res = arr { n - 1 };
    }
     return res;
}
var arr = { 1 , 5 , 2 , 1 , 3 , 2 , 1 };
var n = len ( arr );
System.out.println ( mostFrequent ( arr , n ) );
