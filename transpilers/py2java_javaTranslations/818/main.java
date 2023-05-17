import math;
public void digSum ( n ) {
    var sum = 0;
    while (( n > 0 or sum > 9 )) {
        if (( n == 0 )) {
            n = sum;
            sum = 0;
        }
         sum += n % 10;
        var n = n // 10;
    }
     return sum;
}
n = 1234;
System.out.println ( digSum ( n ) );
