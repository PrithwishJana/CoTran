public void minimumChanges ( arr , n , d ) {
    var maxFreq = - 2147483648;
    freq = {};
    for i in range ( n ) :
        a0 = arr { i } - i * d;
        if (a0 in freq) {
            freq { a0 } += 1;
        }
         else{
            freq { a0 } = 1;
        }
        if (freq { a0 } > maxFreq) {
            maxFreq = freq { a0 };
        }
     return ( n - maxFreq );
}
var n = 5;
var d = 1;
var arr = { 1 , 3 , 3 , 4 , 6 };
var ans = minimumChanges ( arr , n , d );
System.out.println ( ans );
