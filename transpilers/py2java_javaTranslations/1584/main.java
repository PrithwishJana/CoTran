public void countPairs ( n ) {
    var num = ( ( n // 2 ) + 1 );
    var Max = n % num;
    var count = 0;
    for i in range ( 1 , n + 1 ) :
        for j in range ( 1 , n + 1 ) :
            var val = ( ( n % i ) % j ) % n;
            if (( val == Max )) {
                count += 1;
            }
     return count;
}
var n = 5;
System.out.println ( countPairs ( n ) );
