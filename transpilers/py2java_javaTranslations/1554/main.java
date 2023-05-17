public void countBits ( n ) {
    var count = 0;
    while (( n )) {
        count += 1;
        n >>= 1;
    }
     return count;
}
var i = 65;
System.out.println ( countBits ( i ) );
