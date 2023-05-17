public void sumOfDigits ( x ) {
    var sum = 0;
    while (x != 0) {
        sum += x % 10;
        var x = x // 10;
    }
     return sum;
}
public void countNumbers ( l , r ) {
    var count = 0;
    for i in range ( l , r + 1 ) :
        if (i % var 2 == 0 and sumOfDigits ( i ) % 3 == 0) {
            count += 1;
        }
     return count;
}
var l = 1000 ; r = 6000;
System.out.println ( countNumbers ( l , r ) );
