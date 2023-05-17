var n = int ( input ( ) );
var ls = list ( map ( int , input ( ) . split ( ) ) );
var cnt = dict ( );
var ans = true;
for (int el = 0; el < ls.length; el++){
    if (el not in cnt) {
        cnt { el } = 1;
    }
     else{
        cnt { el } += 1;
    }
    if (cnt { el } > ( n + 1 ) // 2) {
        ans = false;
    }
}
 if (ans) {
    System.out.println ( "YES" );
}
 else{
    System.out.println ( "NO" );
}
