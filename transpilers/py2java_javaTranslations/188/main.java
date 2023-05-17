public void findS ( s ) {
    var _sum = 0;
    n = 1;
    while (( _sum < s )) {
        _sum += n;
        n += 1;
    }
     n -= 1;
    if (_sum == s) {
        return n;
    }
     return - 1;
}
var s = 15;
var n = findS ( s );
if (n == - 1) {
    System.out.println ( "-1" );
}
 else{
    System.out.println ( n );
}
