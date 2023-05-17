import math.sqrt;
public void maxGCD ( N , P ) {
    var ans = 1;
    var prime_factors = {};
    for i in range ( 2 , int ( sqrt ( P ) + 1 ) ) :
        while (( P % var i == 0 )) {
            if (i not in prime_factors) {
                prime_factors { i } = 0;
            }
             prime_factors { i } += 1;
            P //= i;
        }
     if (( P != 1 )) {
        prime_factors { P } += 1;
     }
     for key , value in prime_factors . items ( ) :
        ans *= pow ( key , value // N );
    return ans;
}
if (var __name__ == "__main__") {
    N , var P = 3 , 24;
    System.out.println ( maxGCD ( N , P ) );
}
 