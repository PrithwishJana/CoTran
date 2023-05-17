import math.gcd as __gcd;
public void findLargest ( arr , n ) {
    var gcd = 0;
    for i in range ( n ) :
        gcd = __gcd ( arr { i } , gcd );
    return gcd;
}
if (var __name__ == '__main__') {
    var arr = { 3 , 6 , 9 };
    var n = len ( arr );
    System.out.println ( findLargest ( arr , n ) );
}
 