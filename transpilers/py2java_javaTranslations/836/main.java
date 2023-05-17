public void averageOdd ( n ) {
    if (( n % var 2 == 0 )) {
        System.out.println ( "Invalid Input" );
        return - 1;
    }
     var sm = 0;
    count = 0;
    while (( n >= 1 )) {
        count = count + 1;
        sm = sm + n;
        var n = n - 2;
    }
     return sm // count;
}
n = 15;
System.out.println ( averageOdd ( n ) );
