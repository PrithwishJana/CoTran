import math;
public void getSum ( n ) {
    var sm = 0;
    while (( n != 0 )) {
        sm = sm + n % 10;
        var n = n // 10;
    }
     return sm;
}
public void largestDigitSumdivisior ( n ) {
    res = 0;
    for i in range ( 1 , ( int ) ( math . sqrt ( n ) ) + 1 ) :
        if (( n % i == 0 )) {
            res = max ( res , getSum ( i ) );
            res = max ( res , getSum ( n // i ) );
        }
     return res;
}
n = 14;
System.out.println ( largestDigitSumdivisior ( n ) );
