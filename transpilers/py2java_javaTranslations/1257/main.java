public void Digits ( n ) {
    var largest = 0;
    smallest = 9;
    while (( n )) {
        r = n % 10;
        largest = max ( r , largest );
        var smallest = min ( r , smallest );
        var n = n // 10;
    }
     System.out.println ( largest , smallest );
}
n = 2346;
Digits ( n );
