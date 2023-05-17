import sys;
public void minimumX ( n , k ) {
    var mini = sys . maxsize;
    i = 1;
    while (i * i <= n) {
        if (( n % i == 0 )) {
            fir = i;
            sec = n // i;
            num1 = fir * k + sec;
            res = ( num1 // k ) * ( num1 % k );
            if (( res == n )) {
                mini = min ( num1 , mini );
            }
             num2 = sec * k + fir;
            res = ( num2 // k ) * ( num2 % k );
            if (( res == n )) {
                mini = min ( num2 , mini );
            }
         }
         i += 1;
    }
     return mini;
}
if (var __name__ == "__main__") {
    var n = 4;
    k = 6;
    System.out.println ( minimumX ( n , k ) );
    n = 5;
    var k = 5;
    System.out.println ( minimumX ( n , k ) );
}
 