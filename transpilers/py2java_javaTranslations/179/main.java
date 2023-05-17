public void countNumbers ( n ) {
    var k = 0;
    var count = 0;
    while (( n > 0 )) {
        if (( ( n & 1 ) == 0 )) {
            count += pow ( 2 , k );
        }
         k += 1;
        n >>= 1;
    }
     return count;
}
var n = 11;
System.out.println ( countNumbers ( n ) );
