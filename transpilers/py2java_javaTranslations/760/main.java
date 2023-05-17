import fractions.gcd;
import math;
public void LCM ( x , y , z ) {
    var ans = int ( ( x * y ) / ( gcd ( x , y ) ) );
    return int ( ( z * ans ) / ( gcd ( ans , z ) ) );
}
public void findDivisible ( n , x , y , z ) {
    var lcm = LCM ( x , y , z );
    var ndigitnumber = math . pow ( 10 , n - 1 );
    var reminder = ndigitnumber % lcm;
    if (reminder == 0) {
        return ndigitnumber;
    }
     ndigitnumber += lcm - reminder;
    if (ndigitnumber < math . pow ( 10 , n )) {
        return int ( ndigitnumber );
    }
     else{
        return 0;
    }
}
var n = 4;
var x = 2;
var y = 3;
var z = 5;
var res = findDivisible ( n , x , y , z );
if (res != 0) {
    System.out.println ( res );
}
 else{
    System.out.println ( "Not possible" );
}
