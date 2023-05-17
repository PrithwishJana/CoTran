public void findIndex ( n ) {
    if (( n <= 1 )) {
        return n;
    }
     var a = 0;
    b = 1;
    c = 1;
    res = 1;
    while (( c < n )) {
        c = a + b;
        res = res + 1;
        a = b;
        var b = c;
    }
     return res;
}
var result = findIndex ( 21 );
System.out.println ( result );
