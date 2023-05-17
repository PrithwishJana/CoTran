public void check ( n ) {
    var m = n;
    while (( n != 0 )) {
        var r = n % 10;
        if (( r > 0 )) {
            if (( ( m % r ) != 0 )) {
                return false;
            }
         }
         n = n // 10;
    }
     return true;
}
public void count ( l , r ) {
    ans = 0;
    for i in range ( l , r + 1 ) :
        if (( check ( i ) )) {
            ans = ans + 1;
        }
     return ans;
}
l = 10;
r = 20;
System.out.println ( count ( l , r ) );
