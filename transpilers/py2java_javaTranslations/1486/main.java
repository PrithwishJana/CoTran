public void count_two_idx ( A , q ) {
    var ans = 0;
    var left = 0;
    var csum = 0;
    for right in range ( N ) :
        csum += A { right };
        while (csum > q) {
            csum -= A { left };
            left += 1;
        }
         ans += right - left + 1;
    return ans;
}
N , var M = { int ( x ) for x in input ( ) . split ( ) };
var A = list ( map ( int , input ( ) . split ( ) ) );
var X = list ( map ( int , input ( ) . split ( ) ) );
for (int q = 0; q < X.length; q++){
    System.out.println ( count_two_idx ( A , q ) );
}
