import math;
public void findLCM ( arr , n ) {
    var lcm = arr { 0 } ;;
    for i in range ( 1 , n - 1 ) :
        lcm = ( lcm * arr { i } ) / math . gcd ( arr { i } , lcm ) ;;
    return lcm ;;
}
public void countNumbers ( arr , n , l , r ) {
    lcm = int ( findLCM ( arr , n ) ) ;;
    var count = ( r / lcm ) - ( ( l - 1 ) / lcm ) ;;
    System.out.println ( int ( count ) ) ;;
}
var arr = { 1 , 4 , 2 } ;;
var n = len ( arr ) ;;
var l = 1 ;;
var r = 10 ;;
countNumbers ( arr , n , l , r ) ;;
