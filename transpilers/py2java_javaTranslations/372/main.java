import sys;
var input = sys . stdin . readline;
public void solve ( ) {
    n , var k = map ( int , input ( ) . split ( ) );
    var cnt = 1;
    var ans = 0;
    while (cnt <= k and cnt < n) {
        cnt *= 2;
        ans += 1;
    }
     if (cnt >= n) {
        return ans;
     }
     else{
        ans += ( n - cnt ) // k;
        ans += 1 if ( n - cnt ) % k else 0;
        return ans;
    }
}
for _ in range ( int ( input ( ) ) ) :
    System.out.println ( solve ( ) );
