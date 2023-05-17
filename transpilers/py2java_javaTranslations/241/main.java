protected void gcd ( x , y ) {
    if (x > y) {
        var small = y;
    }
     else{
        small = x;
    }
    for i in range ( 1 , small + 1 ) :
        if (( ( x % var i == 0 ) and ( y % i == 0 ) )) {
            var gcd = i;
        }
     return gcd;
}
public void FindLCM ( a , b ) {
    return ( a * b ) / __gcd ( a , b ) ;;
}
public void rangeDivisor ( m , n , a , b ) {
    var lcm = FindLCM ( a , b );
    var a_divisor = int ( n / a - ( m - 1 ) / a );
    var b_divisor = int ( n / b - ( m - 1 ) / b );
    var common_divisor = int ( n / lcm - ( m - 1 ) / lcm );
    var ans = a_divisor + b_divisor - common_divisor;
    return ans;
}
var m = 3;
n = 11;
a = 2;
b = 3 ;;
System.out.println ( rangeDivisor ( m , n , a , b ) );
m = 11;
var n = 1000000;
var a = 6;
var b = 35;
System.out.println ( rangeDivisor ( m , n , a , b ) );
