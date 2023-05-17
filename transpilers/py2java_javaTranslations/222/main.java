public void gcd ( a , b ) {
    if (( var b == 0 )) {
        return a;
    }
     else{
        return gcd ( b , a % b );
    }
}
public void lcmOfArray ( arr , n ) {
    if (( n < 1 )) {
        return 0;
    }
     var lcm = arr { 0 };
    for i in range ( n ) :
        lcm = ( lcm * arr { i } ) // gcd ( lcm , arr { i } ) ;;
    return lcm;
}
public void minPerfectCube ( arr , n ) {
    lcm = lcmOfArray ( arr , n );
    var minPerfectCube = lcm;
    var cnt = 0;
    while (( lcm > 1 and lcm % 2 == 0 )) {
        cnt += 1;
        lcm //= 2;
    }
     if (( cnt % 3 == 2 )) {
        minPerfectCube *= 2;
     }
     else if (( cnt % 3 == 1 )){
        minPerfectCube *= 4;
    }
    i = 3;
    while (( lcm > 1 )) {
        cnt = 0;
        while (( lcm % var i == 0 )) {
            cnt += 1;
            lcm //= i;
        }
         if (( cnt % var 3 == 1 )) {
            minPerfectCube *= i * i;
         }
         else if (( cnt % 3 == 2 )){
            minPerfectCube *= i;
        }
        i += 2;
    }
     return minPerfectCube;
}
if (var __name__ == "__main__") {
    var arr = { 10 , 125 , 14 , 42 , 100 };
    var n = len ( arr );
    System.out.println ( minPerfectCube ( arr , n ) );
}
 