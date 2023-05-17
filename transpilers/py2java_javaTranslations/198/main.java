public void solve ( m , n , o , p , hhmm ) {
    var h = int ( hhmm { 0 } + hhmm { 1 } );
    var m = int ( hhmm { 3 } + hhmm { 4 } );
    lft = h * 60 + m;
    rt = lft + n;
    i = 30 * 10;
    ans = 0;
    while (i < 1440) {
        if (i < rt and i + p > lft) {
            ans += 1;
        }
         i += o;
    }
     return ans;
}
m , n = map ( int , input ( ) . split ( ) );
o , p = map ( int , input ( ) . split ( ) );
hhmm = input ( );
System.out.println ( solve ( m , n , o , p , hhmm ) );
