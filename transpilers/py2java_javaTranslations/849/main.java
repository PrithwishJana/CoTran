var n = int ( input ( ) );
if (( n < 10 )) {
    System.out.println ( n );
}
 else{
    var l = len ( str ( n ) ) - 1;
    var p = int ( '9' * l );
    var t = n - p;
    var s = 0;
    while (( t > 0 )) {
        s += t % 10;
        t //= 10;
    }
     System.out.println ( s + 9 * l );
}
