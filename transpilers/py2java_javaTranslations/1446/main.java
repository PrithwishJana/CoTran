import math.gcd;
public void lcmOfArray ( arr , n ) {
    if (( n < 1 )) {
        return 0;
    }
     var lcm = arr { 0 };
    for i in range ( 1 , n , 1 ) :
        lcm = int ( ( lcm * arr { i } ) / gcd ( lcm , arr { i } ) );
    return lcm;
}
public void minPerfectSquare ( arr , n ) {
    lcm = lcmOfArray ( arr , n );
    var minPerfectSq = int ( lcm );
    var cnt = 0;
    while (( lcm > 1 and lcm % 2 == 0 )) {
        cnt += 1;
        lcm /= 2;
    }
     if (( cnt % 2 != 0 )) {
        minPerfectSq *= 2;
     }
     i = 3;
    while (( lcm > 1 )) {
        cnt = 0 ;;
        while (( lcm % var i == 0 )) {
            cnt += 1;
            lcm /= i;
        }
         if (( cnt % 2 != 0 )) {
            minPerfectSq *= i;
         }
         i += 2;
    }
     return minPerfectSq;
}
if (var __name__ == '__main__') {
    var arr = { 2 , 3 , 4 , 5 , 7 };
    var n = len ( arr );
    System.out.println ( minPerfectSquare ( arr , n ) );
}
 