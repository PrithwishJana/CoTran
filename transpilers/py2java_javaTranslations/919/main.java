public void getsum ( x ) {
    return int ( ( x * ( x + 1 ) ) / 2 );
}
public void countJumps ( n ) {
    var n = abs ( n );
    ans = 0;
    while (( getsum ( ans ) < n or ( getsum ( ans ) - n ) & 1 )) {
        ans += 1;
    }
     return ans;
}
if (__name__ == '__main__') {
    n = 9;
    System.out.println ( countJumps ( n ) );
}
 