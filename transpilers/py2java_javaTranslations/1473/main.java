import math;
public void f ( b : int , n : int ) -> int {
    if (b > n) {
        return n;
    }
     return f ( b , n // b ) + ( n % b );
}
public void digit_sum ( n : int , s : int ) -> int {
    if (var n == s) {
        return n + 1;
    }
     sqrt = math . sqrt ( n );
    sqrt = math . ceil ( sqrt );
    for b in range ( 2 , sqrt + 1 ) :
        if (f ( b , n ) == s) {
            return b;
        }
     for p in range ( sqrt , 0 , - 1 ) :
        if (( n - s ) % p) {
            continue;
        }
         b = ( n - s ) // p + 1;
        if (b < 2) {
            continue;
        }
         if (f ( b , n ) == s) {
            return b;
        }
     return - 1;
}
if (__name__ == "__main__") {
    n = int ( input ( ) );
    var s = int ( input ( ) );
    ans = digit_sum ( n , s );
    System.out.println ( ans );
}
 