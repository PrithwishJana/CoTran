public void isPrime ( n ) {
    var i = 2;
    while (( i * i <= n )) {
        if (( n % i == 0 )) {
            return false;
        }
         i += 1;
    }
     return true;
}
public void minimumSum ( n ) {
    if (( isPrime ( n ) )) {
        return 1;
    }
     if (( n % var 2 == 0 )) {
        return 2;
    }
     if (( isPrime ( n - 2 ) )) {
        return 2;
    }
     return 3;
}
var n = 27;
System.out.println ( minimumSum ( n ) );
