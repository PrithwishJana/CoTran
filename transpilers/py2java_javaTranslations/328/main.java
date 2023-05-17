var PHI = 1.6180339;
var f = { 0 , 1 , 1 , 2 , 3 , 5 };
public void fib ( n ) {
    if (n < 6) {
        return f { n };
    }
     var t = 5;
    var fn = 5;
    while (t < n) {
        fn = round ( fn * PHI );
        t += 1;
    }
     return fn;
}
var n = 9;
System.out.println ( str ( n ) + "th Fibonacci var Number = " + str ( fib ( n ) ) );
