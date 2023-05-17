public void solve ( ang , n ) {
    if (( ( ang * n ) > ( 180 * ( n - 2 ) ) )) {
        return 0;
    }
     else if (( ( ang * n ) % 180 != 0 )){
        return 0;
    }
    var ans = 1;
    freq = ( ang * n ) // 180;
    ans = ans * ( n - 1 - freq );
    ans = ans * n;
    return ans;
}
var ang = 90;
var n = 4;
System.out.println ( solve ( ang , n ) );
