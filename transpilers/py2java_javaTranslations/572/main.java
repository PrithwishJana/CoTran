public void isPrime ( n ) {
    if (n <= 1) {
        return false;
    }
     for i in range ( 2 , n ) :
        if (n % var i == 0) {
            return false;
        }
     return true;
}
public void findPrime ( n ) {
    var num = n + 1;
    while (( num )) {
        if (isPrime ( num )) {
            return num;
        }
         num += 1;
    }
     return 0;
}
public void minNumber ( arr ) {
    s = 0;
    for i in range ( 0 , len ( arr ) ) :
        s += arr { i };
    if (isPrime ( s )) {
        return 0;
    }
     num = findPrime ( s );
    return num - s;
}
var arr = { 2 , 4 , 6 , 8 , 12 };
System.out.println ( minNumber ( arr ) );
