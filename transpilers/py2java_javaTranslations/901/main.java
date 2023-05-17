public void sumOfDigit ( n , b ) {
    var unitDigit = 0;
    sum = 0;
    while (( n > 0 )) {
        unitDigit = n % b;
        sum += unitDigit;
        var n = n // b;
    }
     return sum;
}
n = 50;
var b = 2;
System.out.println ( sumOfDigit ( n , b ) );
