public void getSum ( n ) {
    var sum = 0;
    while (( n != 0 )) {
        sum = sum + int ( n % 10 );
        var n = int ( n / 10 );
    }
     return sum;
}
n = 687;
System.out.println ( getSum ( n ) );
