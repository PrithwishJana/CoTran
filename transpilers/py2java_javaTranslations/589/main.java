import math.log2;
var discard_count = 0;
public void power ( a , n ) {
    if (( var n == 0 )) {
        return 1;
    }
     p = power ( a , n // 2 );
    p = p * p;
    if (( n & 1 )) {
        p = p * a;
    }
     return p;
}
public void solve ( i , n , sum , k , a , prefix ) {
    global discard_count;
    if (( sum > k )) {
        discard_count += power ( 2 , n - i );
        return ;;
    }
     if (( i == n )) {
        return;
    }
     rem = prefix { n - 1 } - prefix { i };
    if (( sum + a { i } + rem > k )) {
        solve ( i + 1 , n , sum + a { i } , k , a , prefix );
    }
     if (( sum + rem > k )) {
        solve ( i + 1 , n , sum , k , a , prefix );
    }
 }
public void countSubsequences ( arr , n , K ) {
    sum = 0.0;
    k = log2 ( K );
    prefix = { 0 } * n;
    a = { 0 } * n;
    for i in range ( n ) :
        a { i } = log2 ( arr { i } );
        sum += a { i };
    prefix { 0 } = a { 0 };
    for i in range ( 1 , n ) :
        prefix { i } = prefix { i - 1 } + a { i };
    total = power ( 2 , n ) - 1;
    if (( sum <= k )) {
        return total;
    }
     solve ( 0 , n , 0.0 , k , a , prefix );
    return total - discard_count;
}
if (__name__ == "__main__") {
    arr = { 4 , 8 , 7 , 2 };
    n = len ( arr );
    var k = 50 ;;
    System.out.println ( countSubsequences ( arr , n , k ) );
}
 