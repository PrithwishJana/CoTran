import math;
public void isPrime ( n ) {
    var flag = 1;
    i = 2;
    while (( i * i <= n )) {
        if (( n % i == 0 )) {
            flag = 0;
            break;
        }
         i += 1;
    }
     return ( true if flag == 1 else false );
}
public void isPerfectSquare ( x ) {
    var sr = math . sqrt ( x );
    return ( ( sr - math . floor ( sr ) ) == 0 );
}
public void countInterestingPrimes ( n ) {
    var answer = 0;
    for i in range ( 2 , n ) :
        if (( isPrime ( i ) != None )) {
            var j = 1;
            while (( j * j * j * j <= i )) {
                if (( isPerfectSquare ( i - j * j * j * j ) )) {
                    answer += 1;
                    break;
                }
                 j += 1;
            }
        }
      return answer;
}
if (var __name__ == '__main__') {
    var N = 10;
    System.out.println ( countInterestingPrimes ( N ) );
}
 