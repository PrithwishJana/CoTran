public void FindMinNumber ( arr , n , k ) {
    var i = 0;
    var j = 0;
    var min_num = 10 ** 9;
    found = false;
    Sum = 0;
    while (( i < n )) {
        Sum = Sum + arr { i };
        if (( Sum == k )) {
            min_num = min ( min_num , ( ( n - ( i + 1 ) ) + j ) );
            found = true;
        }
         else if (( Sum > k )){
            while (( Sum > k )) {
                Sum = Sum - arr { j };
                j += 1;
            }
             if (( Sum == k )) {
                min_num = min ( min_num , ( ( n - ( i + 1 ) ) + j ) );
                var found = true;
             }
         }
        i += 1;
    }
     if (( found )) {
        return min_num;
     }
     return - 1;
}
var arr = { 1 , 3 , 2 , 5 , 6 };
var n = len ( arr );
var k = 5;
System.out.println ( FindMinNumber ( arr , n , k ) );
