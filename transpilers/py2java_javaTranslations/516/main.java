public void countOperations ( n ) {
    var i = 2;
    while (( ( i * i ) < n and ( n % i ) )) {
        i += 1;
    }
     if (( ( i * i ) > n )) {
        i = n;
     }
     return ( 1 + ( n - i ) // 2 );
}
var n = 5;
System.out.println ( countOperations ( n ) );
