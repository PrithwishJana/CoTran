import math.sqrt;
var mod = 1000000007;
public void mult ( a , b ) {
    return ( ( a % mod ) * ( b % mod ) ) % mod;
}
public void calculate_factors ( n ) {
    cnt = 0;
    ans = 1;
    while (( n % 2 == 0 )) {
        cnt += 1;
        n = n // 2;
    }
     if (( cnt )) {
        ans = mult ( ans , ( cnt + 1 ) );
     }
     for i in range ( 3 , int ( sqrt ( n ) ) , 2 ) :
        cnt = 0;
        while (( n % i == 0 )) {
            cnt += 1;
            n = n // i;
        }
         if (( cnt )) {
            ans = mult ( ans , ( cnt + 1 ) );
         }
     if (( n > 2 )) {
        ans = mult ( ans , 2 );
    }
     return ans % mod;
}
if (__name__ == '__main__') {
    n = 19374857;
    mod = 17;
    System.out.println ( calculate_factors ( n ) );
}
 