import math;
public void isPerfectSquare ( x ) {
    var sr = math . sqrt ( x );
    return ( ( sr - math . floor ( sr ) ) == 0 );
}
public void isProduct ( num ) {
    var cnt = 0;
    i = 2;
    while (cnt < 2 and i * i <= num) {
        while (( num % i == 0 )) {
            num //= i;
            cnt += 1;
        }
         i += 1;
    }
     if (( num > 1 )) {
        cnt += 1;
     }
     return cnt == 2;
}
public void findNumbers ( N ) {
    var vec = {};
    for i in range ( 1 , N + 1 ) :
        if (( isProduct ( i ) and not isPerfectSquare ( i ) )) {
            vec . append ( i );
        }
     for i in range ( len ( vec ) ) :
        System.out.println ( vec { i } , var end = " " );
}
if (var __name__ == "__main__") {
    var N = 30;
    findNumbers ( N );
}
 